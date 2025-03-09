import os
import requests
import asyncio
import nest_asyncio
import time
from tqdm import tqdm
from duckduckgo_search import DDGS
from urllib.parse import quote
from pathlib import Path
from docling.document_converter import DocumentConverter
from dotenv import load_dotenv
from lightrag import LightRAG, QueryParam
from lightrag.llm.openai import gpt_4o_mini_complete, gpt_4o_complete, openai_embed
from typing import List, Tuple, Dict, Optional
from concurrent.futures import ThreadPoolExecutor, TimeoutError

# Load environment variables
load_dotenv()

# Apply nest_asyncio to patch the event loop for Jupyter compatibility
try:
    nest_asyncio.apply()
except Exception as e:
    print(f"Warning: Could not apply nest_asyncio: {e}")

# may want to add a query rewriting step first to generate a set of subqueries to search for
def search_duckduckgo(query: str, max_results: int = 10) -> List[Dict]:
    """
    Searches DuckDuckGo for the given query.
    
    Args:
        query (str): The search query
        max_results (int): Maximum number of results to return
        
    Returns:
        List[Dict]: List of search results, each containing 'title', 'body', and 'href'
    """
    print(f"Starting DuckDuckGo search for: {query}")
    with DDGS() as ddgs:
        results = [r for r in ddgs.text(query, max_results=max_results)]
    print(f"Found {len(results)} results")
    return results

def sanitize_folder_name(name: str) -> str:
    """
    Creates a clean folder name by removing special characters and formatting.
    
    Args:
        name (str): The original folder name
        
    Returns:
        str: Sanitized folder name
    """
    # Replace URL encoding with spaces
    name = name.replace('%20', ' ').replace('%', '')
    
    # Remove or replace special characters
    import re
    name = re.sub(r'[^\w\s-]', '', name)
    
    # Replace multiple spaces with single space and strip
    name = ' '.join(name.split())
    
    # Convert to lowercase and limit length
    return name.lower()[:50]

def fetch_and_save_content(
    results: List[Dict],
    query: str,
    html_folder: str = "ddgo_pages",
    md_folder: str = "ddgo_pages_md",
    max_workers: int = 2
) -> Tuple[str, List[str]]:
    """
    Fetches HTML content, converts to Markdown, and saves both versions.
    """
    print(f"Starting content fetch for {len(results)} results")
    start_time = time.time()
    
    # Create folders
    query_folder = sanitize_folder_name(query.replace(" ", "_"))
    query_md_folder = os.path.join(md_folder, query_folder)
    query_html_folder = os.path.join(html_folder, query_folder)
    
    for folder in [html_folder, md_folder, query_md_folder, query_html_folder]:
        Path(folder).mkdir(exist_ok=True)
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    converter = DocumentConverter()
    processed_files = []

    def process_url(result_idx_and_data):
        idx, result = result_idx_and_data
        url = result.get("href")
        if not url:
            return None
            
        try:
            print(f"Processing URL {idx}: {url}")
            base_filename = f"{idx}_{quote(url, safe='')[:100]}"
            html_filepath = os.path.join(query_html_folder, f"{base_filename}.html")
            md_filepath = os.path.join(query_md_folder, f"{base_filename}.md")
            
            # First try to get the HTML
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            # Save HTML first
            with open(html_filepath, 'w', encoding='utf-8') as f:
                f.write(response.text)
            
            # Then convert to markdown
            conversion_result = converter.convert(url)
            markdown_content = conversion_result.document.export_to_markdown()
            
            # Save markdown
            with open(md_filepath, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
                
            print(f"Successfully processed {url}")
            return md_filepath
            
        except Exception as e:
            print(f"Error processing {url}: {str(e)}")
            return None

    # Process URLs in parallel
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = list(executor.map(process_url, enumerate(results, start=1)))
    
    # Filter out None values from failed downloads
    processed_files = [f for f in futures if f is not None]
    
    elapsed = time.time() - start_time
    print(f"Content fetch completed in {elapsed:.2f} seconds. Successfully processed {len(processed_files)} files.")
    
    return query_folder, processed_files


def build_lightrag(
    query: str,
    max_results: int = 2
) -> Tuple[Optional[LightRAG], List[Dict]]:
    """
    Chain the search, fetch, and RAG processing steps together.
    """
    print(f"Starting build_lightrag for query: {query}")
    start_time = time.time()
    
    # Step 1: Search
    results = search_duckduckgo(query, max_results)
    if not results:
        print("No search results found")
        return None, []
    
    # Step 2: Fetch and save content
    query_folder, processed_files = fetch_and_save_content(
        results, 
        query,
        max_workers=2
    )
    
    if not processed_files:
        print("No files were successfully processed")
        return None, []
    
    # Step 3: Initialize LightRAG
    working_dir = f"./lightrag/{query_folder}"
    Path(working_dir).mkdir(exist_ok=True)
    
    print("Initializing LightRAG...")
    try:
        rag = LightRAG(
            working_dir=working_dir,
            embedding_func=openai_embed,
            llm_model_func=gpt_4o_complete
        )
        
        print("LightRAG initialized successfully")
        
        # Step 4: Process documents synchronously
        print(f"Processing {len(processed_files)} documents...")
        for i, md_file in enumerate(processed_files, 1):
            print(f"Processing file {i}/{len(processed_files)}: {md_file}")
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                print(f"File {i}: Read content, length: {len(content)}")
                # Use synchronous insert instead of async
                rag.insert(content)
                print(f"File {i}: Inserted successfully")
        
        print(f"build_lightrag completed in {time.time() - start_time:.2f} seconds")
        return rag, results
            
    except Exception as e:
        print(f"Error during LightRAG processing: {e}")
        import traceback
        traceback.print_exc()
        return None, results
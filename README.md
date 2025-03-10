# chishikAI

chishikAI is your Deep Graph Researcher. Given a research topic, it finds relevant web resources and turn them into a knowledge graph database that you can visualize, query, and expand indefinitely. 

### How to set up to run the notebook chishikAI.ipynb

- clone the repo
- create Python env with requirements.txt
- create .env file with OPENAI_API_KEY
- create an instance on ArangoDB cloud and gets credentials

### Inspiration
ChishikAI was inspired by the need for intuitive knowledge representation. Traditional AI responses often overwhelm users with text, so I aimed to create a tool that visualizes knowledge through interactive graphs, enhancing the research experience.
What it does
ChishikAI is a Deep Graph Researcher that allows users to build knowledge graphs on specific topics. It integrates web research to gather information, enabling users to visualize relationships and receive concise answers to their queries through a multi-agent system.
### How I built it
I developed ChishikAI using:
NetworkX on cuGraph for graph analysis.
LightRAG for knowledge graph construction and semantic querying.
ArangoDB for persistent storage and querying.
LangChain for orchestrating AI agents.
The project involved creating functions for schema generation, web integration, and efficient query handling.
### Challenges I ran into
Key challenges included optimizing the multi-agent system for complex queries and ensuring seamless integration of various technologies. Balancing the cognitive load on agents was crucial to maintain performance and accuracy.
### Accomplishments that I am proud of
I successfully created a functional multi-agent system that provides relevant insights and visualizations. The graph expansion capabilities allows users to expand their knowledge graphs with up-to-date information is also a significant achievement.
### What I learned
I gained valuable insights into knowledge graph technologies, AI orchestration, and the importance of user experience in research tools. I also learned about the complexities of integrating multiple systems for efficient communication.
What's next for ChishikAI - Deep Graph Researcher
### Future plans include:
Optimization of the multi-agent system for improved performance.
Development of a fully fledged app with a user-friendly UI.
Implementation of user-uploaded content features for personalized knowledge enrichment.
Enhancing agentic graph expansion capabilities to autonomously grow knowledge graphs based on user interests.




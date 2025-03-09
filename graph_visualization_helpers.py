import networkx as nx
from pyvis.network import Network
import numpy as np
from pathlib import Path

def calculate_node_importance(G):
    """Calculate node importance using PageRank and degree centrality."""
    pagerank = nx.pagerank(G)
    degrees = dict(G.degree())
    return {node: (0.7 * pagerank[node] + 0.3 * degrees[node]/max(degrees.values()))
            for node in G.nodes()}

def create_network(height="750px", width="100%"):
    """Initialize the Pyvis network with basic settings."""
    net = Network(
        height=height, 
        width=width,
        bgcolor="#ffffff",
        font_color="black",
        directed=False,
        select_menu=False,
        cdn_resources='remote'
    )
    
    # Configure physics with further adjustments for less crowding
    net.force_atlas_2based(
        gravity=-50,
        central_gravity=0.002,  # Further reduced central gravity
        spring_length=200,       # Further increased spring length
        spring_strength=0.03,    # Further reduced spring strength
        damping=0.4,
        overlap=0
    )
    
    # Configure display options
    net.set_options("""
    {
        "nodes": {
            "font": {
                "size": 12,
                "scaling": {
                    "min": 8,
                    "max": 20,
                    "label": {"enabled": true, "min": 8, "max": 20}
                }
            },
            "scaling": {
                "min": 10,
                "max": 50,
                "label": {
                    "enabled": true,
                    "min": 8,
                    "max": 20,
                    "maxVisible": 30,
                    "drawThreshold": 5
                }
            }
        },
        "edges": {
            "color": {"inherit": true},
            "smooth": {"enabled": false},
            "width": 1,
            "scaling": {
                "min": 0.5,
                "max": 4,
                "label": {"enabled": true, "min": 8, "max": 20}
            }
        },
        "physics": {
            "enabled": true,
            "forceAtlas2Based": {
                "gravitationalConstant": -50,
                "centralGravity": 0.01,
                "springLength": 100,
                "springConstant": 0.08,
                "damping": 0.4,
                "avoidOverlap": 0
            },
            "solver": "forceAtlas2Based",
            "stabilization": {
                "enabled": true,
                "iterations": 100,
                "updateInterval": 50
            }
        },
        "interaction": {
            "hover": true,
            "navigationButtons": true,
            "keyboard": {"enabled": true},
            "zoomView": true,
            "hideEdgesOnDrag": true,
            "hideNodesOnDrag": false
        }
    }
    """)
    return net

def add_nodes_to_network(net, G, node_importance):
    """Add nodes to the network with styling based on importance."""
    for node in G.nodes():
        importance = node_importance[node]
        size = 10 + (importance * 40)
        original_id = G.nodes[node].get('original_id', node)
        
        # Extract the numeric part of the node ID for the label
        label = str(node).split('/')[-1]  # Get the last part after the slash
        
        net.add_node(
            node,
            label=label,  # Show only the numeric part of the node ID
            title=str(original_id),  # Show original_id on hover
            size=size,
            color={'background': '#97C2FC', 'border': '#2B7CE9'},
            font={
                'size': 14,  # Font size for visibility
                'strokeWidth': 0,  # No stroke for the font
                'strokeColor': 'white',
                'background': 'white',
                'color': 'black',
                'bold': True,
                'face': 'arial'
            },
            scaling={'label': {'enabled': True, 'min': 8, 'max': 20}},  # Ensure label scaling is enabled
            shape='dot'  # Use 'dot' shape to better fit the label inside
        )

def add_edges_to_network(net, G):
    """Add edges to the network with styling based on weights."""
    for edge in G.edges(data=True):
        weight = float(edge[2].get('d3', 1.0))
        description = edge[2].get('d4', '')
        
        net.add_edge(
            edge[0],
            edge[1],
            value=weight,
            title=f"Weight: {weight}\n{description}",  # Removed edge ID from hover text
            width=weight
        )

def visualize_graph(G, output_path="visualization_output/topic.html"):
    """Main function to create and save the graph visualization.
    
    Args:
        G (networkx.Graph): NetworkX graph object
        output_path (str): Path where the HTML visualization will be saved
    
    Returns:
        Network: The Pyvis network object for display in notebook
    """
    # Calculate importance
    node_importance = calculate_node_importance(G)
    
    # Create network
    net = create_network()
    
    # Add nodes and edges
    add_nodes_to_network(net, G, node_importance)
    add_edges_to_network(net, G)
    
    # Create output directory and save
    Path(output_path).parent.mkdir(exist_ok=True)
    net.save_graph(output_path)
    
    return net 
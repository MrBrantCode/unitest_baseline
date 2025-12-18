"""
QUESTION:
Implement a function named `filter_nodes_in_layer` that takes a graph represented as a dictionary where keys are nodes and values are lists of neighboring nodes, and a positive integer layer number. The function should return a list of nodes that are present in the specified layer of the connected graph. The graph is non-empty and all nodes are reachable from any other node. The layer number represents the distance from the starting nodes (layer 1).
"""

def filter_nodes_in_layer(graph: dict, layer: int) -> list:
    if layer == 1:
        return list(graph.keys())
    
    current_layer = list(graph.keys())
    for _ in range(layer - 1):
        next_layer = []
        for node in current_layer:
            next_layer.extend(graph[node])
        current_layer = list(set(next_layer))  # Use set to avoid duplicates
    
    return current_layer
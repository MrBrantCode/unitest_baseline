"""
QUESTION:
Write a function `compress_graph` that takes an input graph represented as an adjacency list and compresses it according to the following rules: 
1. Remove any isolated nodes (nodes with no edges connecting to them).
2. Merge any nodes that have only one edge connecting them, effectively removing the intermediate node and connecting the nodes at either end directly.
3. Compact the node IDs to ensure that they are contiguous and start from 0.
The function should return the compressed graph in the same format.
The implementation should be able to handle graphs with up to 100,000 nodes and 200,000 edges efficiently.
"""

def compress_graph(graph):
    # Step 1: Remove isolated nodes
    isolated_nodes = [node for node in graph if not graph[node]]
    for node in isolated_nodes:
        del graph[node]

    # Step 2: Merge nodes with only one edge
    for node in list(graph):
        if len(graph[node]) == 1:
            neighbor = graph[node][0]
            del graph[node]
            for n in graph:
                if node in graph[n]:
                    graph[n] = [neighbor if x == node else x for x in graph[n]]

    # Step 3: Compact node IDs
    node_map = {node: i for i, node in enumerate(graph)}
    compressed_graph = {node_map[node]: [node_map[neighbor] for neighbor in neighbors] for node, neighbors in graph.items()}

    return compressed_graph
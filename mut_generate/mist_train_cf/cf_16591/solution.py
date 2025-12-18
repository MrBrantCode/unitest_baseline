"""
QUESTION:
Implement a function called `build_graph` to create a graph using an adjacency list representation. The function should take as input a list of nodes and a list of edges, where each edge is represented as a tuple of two nodes. The function should return a dictionary where each key is a node and its corresponding value is a list of nodes that are directly connected to it. The function should not contain any error checking or handling.
"""

def build_graph(nodes, edges):
    graph = {node: [] for node in nodes}
    for edge in edges:
        graph[edge[0]].append(edge[1])
    return graph
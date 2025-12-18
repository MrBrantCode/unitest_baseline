"""
QUESTION:
Write a function `depth_first_search(graph, start_node)` that performs a depth-first search on a graph and returns a list of all nodes visited, starting from the given node.

The graph is represented as an adjacency list where each key is a node and the corresponding value is a list of nodes that it is connected to. The graph can contain cycles, disconnected components, nodes with no outgoing edges, nodes with no incoming edges, and self-loops. The starting node will always be present in the graph.
"""

def depth_first_search(graph, start_node):
    visited = []
    stack = [start_node]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            neighbors = graph[node]
            stack.extend(neighbors)
    
    return visited
"""
QUESTION:
Write a function called `depth_first_search` that takes in a graph represented as an adjacency list and a starting node, and returns a list of all nodes visited in a depth-first search starting from the given node. The graph can contain cycles, disconnected components, nodes with no outgoing edges, nodes with no incoming edges, and self-loops. The starting node will always be present in the graph.
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
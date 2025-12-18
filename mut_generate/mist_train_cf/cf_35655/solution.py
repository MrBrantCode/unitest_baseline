"""
QUESTION:
Implement a Python generator function named `generate_paths` that takes in a directed acyclic graph (represented as an adjacency list), a start node, and an end node, and yields all possible paths from the start node to the end node as lists of nodes in the order they are visited. 

The graph, start node, and end node are represented as strings, and the function should handle cases where the start or end node is not in the graph.
"""

def generate_paths(graph, start, end):
    def dfs(current, path):
        if current == end:
            yield path + [current]
        else:
            for neighbor in graph.get(current, []):
                yield from dfs(neighbor, path + [current])
    
    if start not in graph or end not in graph:
        return
    
    yield from dfs(start, [])
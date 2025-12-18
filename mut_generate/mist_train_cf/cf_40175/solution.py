"""
QUESTION:
Implement a function named `all_paths` that generates all possible paths in a given graph from a starting node to an ending node. The graph is represented using an adjacency list, where each node is associated with a list of its neighboring nodes. The function takes the graph, the starting node, and the ending node as input, and returns a list of all possible paths from the starting node to the ending node. The graph is represented as a dictionary where keys are nodes and values are lists of neighboring nodes.
"""

def all_paths(graph, start, end):
    def find_paths(current, end, path, visited, all_paths):
        visited[current] = True
        path.append(current)
        if current == end:
            all_paths.append(path.copy())
        else:
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    find_paths(neighbor, end, path, visited, all_paths)
        path.pop()
        visited[current] = False

    all_paths = []
    visited = {node: False for node in graph}
    find_paths(start, end, [], visited, all_paths)
    return all_paths
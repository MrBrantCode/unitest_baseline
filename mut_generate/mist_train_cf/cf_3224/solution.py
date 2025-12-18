"""
QUESTION:
Write a function `dfs(graph, start_node)` that takes in a graph represented as an adjacency list and a starting node, and returns a list of all nodes visited in a depth-first search starting from the given node. The graph can contain cycles, disconnected components, self-loops, and nodes with no outgoing or incoming edges. The starting node is guaranteed to be present in the graph. The function should handle duplicate nodes and edges, as well as weighted edges.
"""

def dfs(graph, start_node):
    visited = set()  
    stack = [start_node]  

    while stack:
        node = stack.pop()  

        if node not in visited:
            visited.add(node)  
            neighbors = graph[node]  

            for neighbor in neighbors:
                stack.append(neighbor[0])  

    return list(visited)
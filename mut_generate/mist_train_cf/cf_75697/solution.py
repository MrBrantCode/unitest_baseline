"""
QUESTION:
Implement a function named `dfs` that performs a depth-first search on a graph. The function should take two parameters: `graph` and `start`. The `graph` is represented as a dictionary where each key is a node and its corresponding value is a set of neighboring nodes. The `start` parameter is the node to begin the search from. The function should return a set of all visited nodes. Implement this function without using recursion, instead utilizing a stack data structure.
"""

def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node] - visited)
    return visited
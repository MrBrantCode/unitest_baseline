"""
QUESTION:
Write a function `dfs` that takes in a graph represented as a dictionary where each key is a node and its corresponding value is a set of neighboring nodes, and a starting node, and returns a list of all nodes visited in a depth-first search starting from the given node. The function should not revisit any node.
"""

def dfs(graph, start):
    visited = []  # List to keep track of visited nodes
    stack = [start]  # Initialize stack with starting node

    while stack:
        node = stack.pop()  # Pop the last node from the stack
        if node not in visited:
            visited.append(node)  # Add node to the visited list
            stack.extend(graph[node] - set(visited))  # Add unvisited neighbors to the stack

    return visited
"""
QUESTION:
Implement the depth-first search (DFS) algorithm for a directed graph represented as an adjacency list to return the nodes in the order they were visited. The graph is represented as a dictionary where keys are integers representing the nodes, and the values are sets of integers representing the neighboring nodes.

Complete the `dfs` function with the following signature:
`def dfs(adjacency: dict, start_node: int) -> List[int]:`

Input:
- `adjacency` (dict): A dictionary representing the adjacency list of the directed graph.
- `start_node` (int): The integer representing the starting node for the DFS traversal.

Output:
- Returns a list of integers representing the nodes visited in the order of traversal.

Restrictions:
- Use a set to keep track of visited nodes.
- Use a stack to traverse the graph.
- The provided code snippet should be utilized in the implementation.
"""

from typing import List

def dfs(adjacency: dict, start_node: int) -> List[int]:
    visited = set()
    ordering = []
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            ordering.append(node)
            # add the unvisited neighbors to the stack
            unvisited_neighbors = adjacency[node] - visited
            for neighbor in unvisited_neighbors:
                stack.append(neighbor)

    return ordering
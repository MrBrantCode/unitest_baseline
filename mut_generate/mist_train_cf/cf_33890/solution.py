"""
QUESTION:
Implement a function `dfsTraversal(startNode, graph)` that performs a depth-first search (DFS) traversal on a graph and returns a list of integers representing the order in which the nodes are discovered. The graph is represented as an adjacency list, where `graph[i]` is a list of integers representing the nodes adjacent to node `i`. The function should take as input an integer `startNode` representing the starting node for the DFS traversal and the adjacency list `graph`.
"""

def dfsTraversal(startNode, graph):
    visited = set()
    traversal_order = []

    def dfs(node):
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            for neighbor in graph[node]:
                dfs(neighbor)

    dfs(startNode)
    return traversal_order
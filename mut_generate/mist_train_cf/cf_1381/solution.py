"""
QUESTION:
Implement a function `dfs(graph, start_node)` that performs a depth-first search (DFS) traversal on a directed graph with weighted edges represented using an adjacency list. The function should return the order in which the nodes are visited during the traversal. 

The function should handle cases where the graph is cyclic, and return an error message "Cycle detected in the graph." if a cycle is detected. Additionally, it should handle cases where the graph is empty or the starting node is not present in the graph, and return an error message "Start node is not present in the graph." in the latter case.

The function should have a time complexity of O(V + E) and a space complexity of O(V), where V is the number of vertices (nodes) and E is the number of edges in the graph.
"""

def dfs(graph, start_node):
    if start_node not in graph:
        return "Start node is not present in the graph."

    visited = set()
    stack = [start_node]
    traversal_order = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            if node in graph:
                # Sort the adjacent nodes based on their weights (if applicable)
                adjacent_nodes = sorted(graph[node], key=lambda x: x[1], reverse=True)
                for adjacent_node, _ in adjacent_nodes:
                    if adjacent_node not in visited:
                        stack.append(adjacent_node)
        else:
            return "Cycle detected in the graph."

    return traversal_order
"""
QUESTION:
Implement a function `dfs(graph, start_node)` that performs a Depth-First-Search (DFS) traversal on a given directed graph with weighted edges. The graph is represented using an adjacency list. The function should return the order in which the nodes are visited during the DFS traversal. If a cycle is detected, the function should return an error message.

The function should handle the cases where the graph is empty or the starting node is not present in the graph. The function should also handle the case where the graph contains cycles.

The input graph is an adjacency list where each key is a node and its corresponding value is a list of tuples, where each tuple contains an adjacent node and the weight of the edge. The function should sort the adjacent nodes based on their weights in descending order before visiting them.

The function should have a time complexity of O(V + E), where V is the number of vertices (nodes) and E is the number of edges in the graph. The function should have a space complexity of O(V), where V is the number of vertices.
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
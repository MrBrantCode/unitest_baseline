"""
QUESTION:
Implement a function `dfs` that performs a depth-first search on a directed acyclic graph (DAG). The function should take a dictionary representing the graph, where each key is a unique node identifier and each value is an object with an `identifier` attribute and a `neighbors` attribute. The function should return a tuple containing a list of all visited nodes in the order they were visited and the average depth level of the visited nodes. The function should be optimized for time complexity and handle disconnected graphs.
"""

from collections import defaultdict

class Node:
    def __init__(self, identifier):
        self.identifier = identifier
        self.neighbors = []

def dfs(graph):
    visited = set()
    depth_sum = 0
    depth_count = 0
    traversal_order = []

    def visit(node, depth):
        nonlocal depth_sum, depth_count
        visited.add(node)
        traversal_order.append(node.identifier)
        depth_sum += depth
        depth_count += 1

        for neighbor in node.neighbors:
            if neighbor not in visited:
                visit(neighbor, depth + 1)

    for node in graph.values():
        if node not in visited:
            visit(node, 0)

    average_depth = depth_sum / depth_count if depth_count > 0 else 0
    return traversal_order, average_depth
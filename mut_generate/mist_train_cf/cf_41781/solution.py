"""
QUESTION:
Implement a `dijkstra` function that calculates the shortest path between two nodes in a directed graph using Dijkstra's algorithm. The function should take as input a graph represented as an adjacency list (`graph`), a start node (`start`), and an end node (`end`), and return the shortest path as a list of nodes and the total distance of the path.

The graph is represented as a dictionary where each key is a node and its corresponding value is a list of tuples, each tuple containing a neighboring node and the weight of the edge between them. The function should use a priority queue to efficiently explore the graph.

Restrictions: The graph may contain cycles and the function should handle cases where there is no path between the start and end nodes.
"""

from collections import defaultdict
import heapq

def dijkstra(graph, start, end):
    pq = [(0, start, [])]
    visited = set()

    while pq:
        (cost, node, path) = heapq.heappop(pq)
        if node not in visited:
            path = path + [node]
            if node == end:
                return path, cost
            visited.add(node)
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (cost + weight, neighbor, path))
    return [], float('inf')
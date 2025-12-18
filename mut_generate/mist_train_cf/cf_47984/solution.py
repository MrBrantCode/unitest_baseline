"""
QUESTION:
Implement a function named `shortest_path` that takes a graph represented as an adjacency list, a start node, and an end node as inputs. The graph can have weighted edges and cycles. The function should return the shortest distance and the corresponding path from the start node to the end node. Assume the graph is connected and all edge weights are nonnegative.
"""

from heapq import heappop, heappush
from collections import defaultdict

def shortest_path(graph, start, end):
    queue = [(0, start, [])]
    seen = set()
    min_dist = defaultdict(int)
    while queue:
        (cost, node, path) = heappop(queue)
        if node not in seen:
            seen.add(node)
            path = path + [node]
            if node == end:
                return cost, path
            for c, neighbour in graph.get(node, []):
                if neighbour not in seen:
                    old_cost = min_dist.get(neighbour, None)
                    new_cost = cost + c
                    if old_cost is None or new_cost < old_cost:
                        min_dist[neighbour] = new_cost
                        heappush(queue, (new_cost, neighbour, path))
    return float("inf")
"""
QUESTION:
Implement the `dijkstra_shortest_path` function, which takes a directed graph `graph`, a `source` node, and a `target` node as input. The graph is represented as a dictionary where the keys are the nodes and the values are lists of tuples representing the outgoing edges and their associated weights. The function should return a tuple `(path, distance)`, where `path` is a list of nodes representing the shortest path from the source to the target, and `distance` is the total weight of the shortest path. The function should use Dijkstra's algorithm to find the shortest path from the source to the target node in the given graph.
"""

import heapq

def dijkstra_shortest_path(graph, source, target):
    distances = {node: float('inf') for node in graph}
    distances[source] = 0

    queue = [(0, source, [])]

    while queue:
        cur_dist, cur_node, cur_path = heapq.heappop(queue)

        if cur_node == target:
            return cur_path + [cur_node], cur_dist

        for neighbor, weight in graph[cur_node]:
            new_dist = cur_dist + weight

            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(queue, (new_dist, neighbor, cur_path + [cur_node]))

    return None, float('inf')
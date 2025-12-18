"""
QUESTION:
Implement a function `bellman_ford(n, edges, source)` that takes the number of nodes `n`, a list of directed edges `edges` where each edge is represented as a tuple `(a, b, c)` with `a` and `b` being the nodes connected by the edge and `c` being the weight of the edge, and the source node `source`. The function should return a list of length `n` representing the shortest distance from the `source` node to all other nodes. If there is no path from the `source` node to a particular node, the distance should be represented as infinity.
"""

def bellman_ford(n, edges, source):
    distance = [float('inf')] * n
    distance[source] = 0

    for _ in range(n - 1):
        for a, b, c in edges:
            if distance[a] + c < distance[b]:
                distance[b] = distance[a] + c

    for a, b, c in edges:
        if distance[a] + c < distance[b]:
            return "Graph contains negative cycle"

    return distance
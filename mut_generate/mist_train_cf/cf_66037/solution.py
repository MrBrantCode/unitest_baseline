"""
QUESTION:
Write a function `maxProbability(n, edges, succProb, start, end)` that takes the following parameters:

- `n`: The number of nodes in an undirected weighted graph.
- `edges`: A list of undirected edges where `edges[i] = [a, b]` represents an edge between nodes `a` and `b`.
- `succProb`: A list of probabilities where `succProb[i]` is the probability of successful traversal for the edge `edges[i]`.
- `start` and `end`: The start and end nodes.

The function should return the maximum probability of successful traversal from `start` to `end` and the corresponding path. If no path exists, return 0 and an empty list.

Constraints:
- `2 <= n <= 10^4`
- `0 <= start, end < n`
- `start != end`
- `0 <= a, b < n`
- `a != b`
- `0 <= succProb.length == edges.length <= 2*10^4`
- `0 <= succProb[i] <= 1`
- Each pair of nodes is connected by at most one edge.
"""

import collections
import heapq

def maxProbability(n, edges, succProb, start, end):
    graph = collections.defaultdict(list)
    for (a, b), prob in zip(edges, succProb):
        graph[a].append((b, prob))
        graph[b].append((a, prob))

    best_prob = [0.0] * n
    best_prob[start] = 1.0
    visited = set()
    queue = [(-1.0, start, [start])]

    while queue:
        prob, node, path = heapq.heappop(queue)
        prob *= -1
        if node not in visited:
            visited.add(node)
            if node == end:
                return prob, path
            for neigh, edge_prob in graph[node]:
                if neigh not in visited:
                    new_prob = prob * edge_prob
                    if new_prob > best_prob[neigh]:
                        best_prob[neigh] = new_prob
                        heapq.heappush(queue, (-new_prob, neigh, path + [neigh]))

    return 0.0, []
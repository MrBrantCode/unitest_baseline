"""
QUESTION:
Write a function `maxProbability` that takes in an integer `n`, an edge list `edges`, an array `succProb` of corresponding edge probabilities, a start node `start`, and an end node `end`, and returns the maximum probability of successful traversal from `start` to `end` in an undirected weighted graph. The function should return 0 if no path exists between `start` and `end`. The input constraints are: `2 <= n <= 10^4`, `0 <= start, end < n`, `start != end`, `0 <= a, b < n`, `a != b`, `0 <= succProb.length == edges.length <= 2*10^4`, `0 <= succProb[i] <= 1`.
"""

import heapq
from collections import defaultdict
def maxProbability(n, edges, succProb, start, end):
    graph = defaultdict(list)
    for (src, dst), prob in zip(edges, succProb):
        graph[src].append((dst, prob))
        graph[dst].append((src, prob))
    max_prob = [0] * n
    max_prob[start] = 1
    pq = [(-1, start)]  # Use negative prob to sort max first
    while pq:
        prob, node = heapq.heappop(pq)
        prob = -prob
        if prob < max_prob[node]: # Skip because we have already found a better way
            continue
        for neighbor, neighbor_prob in graph[node]:
            new_prob = prob * neighbor_prob
            if new_prob > max_prob[neighbor]:
                max_prob[neighbor] = new_prob
                heapq.heappush(pq, (-new_prob, neighbor))
    return max_prob[end]
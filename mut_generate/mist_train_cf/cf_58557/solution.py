"""
QUESTION:
You are given a 2D integer array `edges` representing an undirected star graph with `n` nodes, where each `edges[i] = [ui, vi]` signifies the existence of an edge between nodes `ui` and `vi`. The function `findCenter` should return the central node of the given star graph, which is the node connected to all other nodes.

Constraints: 
- 3 <= n <= 10^5
- edges.length == n - 1
- edges[i].length == 2
- 1 <= ui, vi <= n
- ui != vi
"""

from collections import Counter

def findCenter(edges):
    count = Counter()
    for edge in edges:
        u, v = edge
        count[u] += 1
        count[v] += 1
    for node, cnt in count.items():
        if cnt == len(edges):
            return node
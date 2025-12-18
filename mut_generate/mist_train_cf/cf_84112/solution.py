"""
QUESTION:
Given a directed acyclic graph with `n` vertices numbered from `0` to `n-1`, an array `edges` where `edges[i] = [fromi, toi]` represents a directed edge from node `fromi` to node `toi`, and an integer `k` representing the maximum path length, write a function `findSmallestSetOfVertices(n, edges, k)` to find the smallest set of vertices from which all nodes in the graph are reachable within `k` steps. The function should return a list of vertices in any order.

Constraints: `2 <= n <= 10^5`, `1 <= edges.length <= min(10^5, n * (n - 1) / 2)`, `edges[i].length == 2`, `0 <= fromi, toi < n`, All pairs `(fromi, toi)` are distinct, `1 <= k <= n`.
"""

from collections import defaultdict
from typing import List

def findSmallestSetOfVertices(n: int, edges: List[List[int]], k: int) -> List[int]:
    incomingEdges = defaultdict(int)
    for s, e in edges:
        incomingEdges[e] += 1
    return [i for i in range(n) if incomingEdges[i] == 0]
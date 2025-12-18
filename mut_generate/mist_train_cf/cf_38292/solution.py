"""
QUESTION:
Write a function `shortest_distances` that takes the adjacency list `G` of a directed graph with `N` nodes as input and returns a list of length `N`, where the `i`-th element represents the shortest distance from node 0 to node `i`. If a node is unreachable from node 0, its distance should be -1. The graph may contain self-loops and multiple edges between the same pair of nodes. The input constraints are 1 <= `N` <= 10^5 and 0 <= `M` <= 10^5, where `M` is the number of edges in the graph.
"""

from typing import List

def shortest_distances(G: List[List[int]]) -> List[int]:
    N = len(G)
    dist = [-1] * N
    nodes = [[] for _ in range(N)]

    dist[0] = 0
    nodes[0] = [0]

    for k in range(1, N):
        for v in nodes[k-1]:
            for next_v in G[v]:
                if dist[next_v] != -1:
                    continue
                dist[next_v] = dist[v] + 1
                nodes[k].append(next_v)

    return dist
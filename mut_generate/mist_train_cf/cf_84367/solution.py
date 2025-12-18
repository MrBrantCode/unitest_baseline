"""
QUESTION:
Given a star graph represented as a 2D integer array `edges` where each sub-array `edges[i] = [ui, vi]` signifies an edge between nodes `ui` and `vi`, find the central node of the graph. The central node is the node that is directly connected to all other nodes in the graph. The function to solve this problem is `findCenter(edges)`.

The input `edges` has the following properties: `3 <= n <= 10^5`, `edges.length == n - 1`, `edges[i].length == 2`, `1 <= ui, vi <= n`, and `ui != vi`. The provided `edges` constitute a valid star graph.
"""

def findCenter(edges):
    freq = {}
    for edge in edges:
        for node in edge:
            if node in freq:
                freq[node] += 1
            else:
                freq[node] = 1
    for node, count in freq.items():
        if count == len(edges):
            return node
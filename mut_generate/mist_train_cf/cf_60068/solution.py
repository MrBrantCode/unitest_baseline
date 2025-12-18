"""
QUESTION:
Write a function named `minMalwareSpread` that takes an `n x n` adjacency matrix `graph` and a list of initially infected nodes `initial` as input, and returns the node that, when removed, would minimize the final count of infected nodes in the entire network. If there are multiple such nodes, return the one with the smallest index. Assume `n` is in the range [2, 300], `graph[i][j]` is 0 or 1, `graph[i][j] == graph[j][i]`, `graph[i][i] == 1`, and `1 <= initial.length <= n`. All integers in `initial` are unique.
"""

from collections import defaultdict, Counter

def minMalwareSpread(graph, initial):
    N = len(graph)
    def dfs(node, color):
        colors[node] = color
        for nei, adj in enumerate(graph[node]):
            if adj and nei != node and colors[nei] == -1:
                dfs(nei, color)

    colors = [-1] * N
    color = 0
    for node in range(N):
        if colors[node] == -1:
            dfs(node, color)
            color += 1

    size = Counter(colors[i] for i in initial)
    color_count = Counter(colors)

    ans = float('inf')
    for node in sorted(initial):
        c = colors[node]
        if size[c] == 1:
            if ans == float('inf'):
                ans = node
            elif color_count[colors[ans]] < color_count[c]:
                ans = node
            elif color_count[colors[ans]] == color_count[c] and node < ans:
                ans = node

    if ans == float('inf'):
        return min(initial)
    return ans
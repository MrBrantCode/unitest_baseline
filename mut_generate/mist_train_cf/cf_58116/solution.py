"""
QUESTION:
Write a function `minTime` that takes four parameters: `n`, `edges`, and `hasApple`. The function should return the minimum time in seconds needed to collect all apples in a tree, starting at vertex 0 and coming back to this vertex.

The tree consists of `n` vertices numbered from `0` to `n-1` and has some apples in their vertices. The time to walk over one edge of the tree varies. The edges of the undirected tree are given in the array `edges`, where `edges[i] = [ai, bi, wi]` means that there exists an edge connecting the vertices `ai` and `bi` with a weight of `wi` representing the time it takes to traverse this edge. Additionally, there is a boolean array `hasApple`, where `hasApple[i] = true` means that vertex `i` has an apple; otherwise, it does not have any apple.

Constraints:
`1 <= n <= 10^5`
`edges.length == n - 1`
`edges[i].length == 3`
`0 <= ai < bi <= n - 1`
`hasApple.length == n`
`1 <= wi <= 100`
"""

def minTime(n, edges, hasApple):
    graph = {}
    for u, v, w in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    def dfs(node, parent):
        total = 0
        for child, cost in graph[node]:
            if child == parent:
                continue
            minCost = dfs(child, node)
            if minCost > 0 or hasApple[child]:
                total += minCost + cost
        if not (node == 0 or hasApple[node] or total > 0):
            return 0
        return total
    
    return dfs(0, -1) * 2
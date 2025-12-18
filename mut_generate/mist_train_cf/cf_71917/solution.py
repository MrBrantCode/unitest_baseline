"""
QUESTION:
Write a function `isTree(graph)` to determine if an undirected graph is a tree. The graph is represented by an array `graph`, where `graph[u]` is an array of nodes that node `u` is adjacent to. The function should return `True` if and only if the graph is a tree, i.e., it is connected and there is exactly one path between any two nodes. Assume the graph has `n` nodes numbered between `0` and `n - 1`, `1 <= n <= 100`, and the graph may not be connected.
"""

def entrance(graph):
    def dfs(v, p):
        visited[v] = True
        for u in graph[v]:
            if u == p: continue
            if visited[u] or not dfs(u, v): return False
        return True
    
    visited = [False] * len(graph)
    return dfs(0, -1) and all(visited)
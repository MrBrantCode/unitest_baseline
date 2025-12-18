"""
QUESTION:
Given an undirected graph with `n` nodes and weighted edges, determine if the graph is a tree and return its total weight if it is, or -1 if it's not. 

Write a function `isTree` that takes as input two parameters: `graph` and `weights`. `graph` is a 2D array where `graph[u]` is an array of nodes adjacent to node `u`, and `weights` is a 2D array where `weights[u][v]` is the weight of the edge between `u` and `v`. 

The function should return a list containing either the total weight of the tree if it is a tree, or -1 if it's not. The graph is a tree if it is connected and there is exactly one path between any two nodes. 

Constraints:
- `graph.length == n`
- `1 <= n <= 100`
- `0 <= graph[u].length <= n`
- `0 <= graph[u][i] <= n - 1`
- `graph[u]` does not contain `u`.
- All the values of `graph[u]` are unique.
- If `graph[u]` contains `v`, then `graph[v]` contains `u`.
- `weights.length == n`
- `weights[u].length == n`
- `0 <= weights[u][v] <= 1000`
- `weights[u][v] == weights[v][u]`
"""

def isTree(graph, weights):
    visited = [False] * len(graph)

    def dfs(node, parent):
        visited[node] = True
        for neighbor in graph[node]:
            if visited[neighbor]:
                if neighbor != parent:
                    return False
            else:
                if not dfs(neighbor, node):
                    return False
        return True

    def total_weight():
        weight_sum = 0
        for u in range(len(graph)):
            for v in graph[u]:
                weight_sum += weights[u][v]
        # Since each edge is counted twice (once for each node), divide the total sum by 2
        return weight_sum // 2
        
    if not dfs(0, -1):
        return [-1]
            
    for visit in visited:
        if not visit:
            return [-1]
    return [total_weight()]
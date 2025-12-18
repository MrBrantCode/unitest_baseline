"""
QUESTION:
Write a function `isBipartite(graph)` to determine if an undirected graph is bipartite. The graph is represented as a 2D array where `graph[u]` is an array of nodes adjacent to node `u`. The function should return `true` if the graph is bipartite and `false` otherwise.

The graph has the following properties: 
- `graph.length == n` where `n` is the number of nodes
- `1 <= n <= 100`
- `0 <= graph[u].length < n`
- `0 <= graph[u][i] < n - 1`
- No self-edges exist (`graph[u]` does not include `u`)
- No parallel edges are present (`graph[u]` does not have duplicate values)
- If `v` is in `graph[u]`, then `u` is in `graph[v]` (the graph is undirected)
"""

def isBipartite(graph):
    n = len(graph)
    color = [0] * n
    for i in range(n):
        if color[i] == 0:
            stack = [i]
            color[i] = 1
            while stack:
                node = stack.pop()
                for neighbour in graph[node]:
                    if color[neighbour] == 0:
                        stack.append(neighbour)
                        color[neighbour] = -color[node]
                    elif color[neighbour] == color[node]:
                        return False
    return True
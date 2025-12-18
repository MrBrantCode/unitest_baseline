"""
QUESTION:
Write a function `max_quartet_degree(n, edges)` that takes an integer `n` and an array `edges` where each `edges[i] = [ui, vi]` represents an undirected edge between `ui` and `vi` in a graph. The function should return the maximum degree of a connected quartet in the graph, or `-1` if the graph has no connected quartets.

The degree of a connected quartet is the number of edges where one endpoint is in the quartet and the other is not. The function should be able to handle a graph with `4 <= n <= 500` nodes and `1 <= edges.length <= n * (n-1) / 2` edges, where `1 <= ui, vi <= n` and `ui != vi`, with no repeated edges.
"""

def max_quartet_degree(n, edges):
    graph = [[] for _ in range(n + 1)]
    degrees = [0] * (n + 1)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        degrees[u] += 1
        degrees[v] += 1

    max_degree = -1
    for i in range(1, n + 1):
        graph[i].sort(key = lambda j: degrees[j])
        common = {j for j in graph[i]}
        for j in reversed(graph[i]):
            if degrees[i] + degrees[j] - len(common) > max_degree:
                for k in graph[j]:
                    if k in common:
                        for l in common:
                            if degrees[i] + degrees[j] + degrees[k] + degrees[l] - len({i,j,k,l}) > max_degree:
                                max_degree = degrees[i] + degrees[j] + degrees[k] + degrees[l] - len({i,j,k,l})
                common.remove(j)

    return max_degree if max_degree > 0 else -1
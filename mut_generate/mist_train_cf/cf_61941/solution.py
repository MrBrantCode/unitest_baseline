"""
QUESTION:
Implement the function `maxNumEdgesToRemove(n, edges)` where `n` is the number of nodes in the graph and `edges` is an array of edges where `edges[i] = [typei, ui, vi]` represents a bidirectional edge of type `typei` connecting nodes `ui` and `vi`. Return the maximum number of edges that can be eliminated while ensuring the graph remains fully traversable by both Alice and Bob, or return `-1` if it's unfeasible. The constraints are `1 <= n <= 10^5`, `1 <= edges.length <= min(10^5, 3 * n * (n-1) / 2)`, `edges[i].length == 3`, `1 <= edges[i][0] <= 3`, and `1 <= edges[i][1] < edges[i][2] <= n`. All tuples `(typei, ui, vi)` are unique.
"""

def maxNumEdgesToRemove(n, edges):
    parent = list(range(n+1)) 
    size = [1] * (n+1)

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x, y = find(x), find(y)
        if x == y:
            return 0
        if size[x] < size[y]:
            x, y = y, x
        parent[y] = x
        size[x] += size[y]
        return 1

    edges.sort(reverse=True)
    res = sum(union(u,v) for t,u,v in edges)
    return -1 if size[find(1)] != n else len(edges) - res
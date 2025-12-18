"""
QUESTION:
You are given an undirected graph with `n` nodes, an array `edgeList` representing the edges between nodes with distances, and an array `queries` of paths to be verified. The task is to create a function named `edgeLengthRestrictedPaths` that returns a boolean array where each value corresponds to whether a path for a query exists such that every edge on the path has a distance strictly less than the given limit.

`edgeLengthRestrictedPaths` function should take three parameters: `n`, `edgeList`, and `queries`. The `edgeList` parameter is a 2D array where `edgeList[i] = [ui, vi, disi]` represents an edge between nodes `ui` and `vi` with a distance of `disi`. The `queries` parameter is a 2D array where `queries[j] = [pj, qj, limitj]` represents a query for a path between `pj` and `qj` with a distance limit of `limitj`. The function should return a boolean array `answer` of length `queries.length` where `answer[j]` is `true` if a path for `queries[j]` exists, and `false` if it does not.

Constraints: `2 <= n <= 10^5`, `1 <= edgeList.length, queries.length <= 10^5`, `edgeList[i].length == 3`, `queries[j].length == 3`, `0 <= ui, vi, pj, qj <= n - 1`, `ui != vi`, `pj != qj`, `1 <= disi, limitj <= 10^9`.
"""

def edgeLengthRestrictedPaths(n, edgeList, queries):
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank   = [0] * n

        def find(self, x):
            if x != self.parent[x]:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x, y):
            rx, ry = self.find(x), self.find(y)
            if rx != ry:
                if self.rank[rx] > self.rank[ry]:
                    self.parent[ry] = rx
                else:
                    self.parent[rx] = ry
                    if self.rank[rx] == self.rank[ry]:
                        self.rank[ry] += 1

    edges = [(d, u, v) for u, v, d in edgeList]
    edges.sort(reverse=True)

    query_with_index = [(limit, p, q, i)
                        for i, (p, q, limit) in enumerate(queries)]
    query_with_index.sort(key=lambda t: t[0], reverse=True)

    uf = UnionFind(n)
    ans = [None] * len(queries)

    pointer_edges = 0

    for limit, p, q, i in query_with_index:
        while pointer_edges < len(edges) and edges[pointer_edges][0] >= limit:
            _, u, v = edges[pointer_edges]
            uf.union(u, v)
            pointer_edges += 1
        ans[i] = (uf.find(p) == uf.find(q))

    return ans
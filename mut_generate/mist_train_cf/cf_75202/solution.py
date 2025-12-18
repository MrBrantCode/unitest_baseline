"""
QUESTION:
Write a function named `numComponents` that takes as input an integer `n` and a 2D array `edges` where each element `edges[i] = [ai, bi, wi]` represents an edge between `ai` and `bi` with weight `wi`, and an integer `k`. The function should return the number of connected components in the graph where the total weight of the edges in each component exceeds `k`. The graph has `n` nodes, `1 <= n <= 2000`, `1 <= edges.length <= 5000`, `edges[i].length == 3`, `0 <= ai < bi < n`, `ai != bi`, `1 <= wi <= 100`, and no edges are repeated.
"""

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.weights = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y, weight):
        rootx, rooty = self.find(x), self.find(y)
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                rootx, rooty = rooty, rootx
            self.parent[rooty] = rootx
            self.weights[rootx] += self.weights[rooty] + weight
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1

    def components(self, k):
        return len([weight for weight in self.weights if weight > k])

def numComponents(n, edges, k):
    uf = UnionFind(n)

    for ai, bi, wi in sorted(edges, key = lambda x : -x[2]):
        uf.union(ai, bi, wi)

    return uf.components(k)
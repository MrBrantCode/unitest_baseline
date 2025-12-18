"""
QUESTION:
Implement the `kruskal_mst` function that takes a list of undirected graph edges as input, where each edge is represented as a tuple of (source, destination, weight), and returns a list of tuples representing the edges of the minimum spanning tree. The input graph is connected and weighted, and the function should use Kruskal's algorithm.
"""

class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1


def kruskal_mst(edges):
    edges.sort(key=lambda x: x[2])  # Sort edges by weight
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])

    disjoint_set = DisjointSet(vertices)
    mst = []
    for edge in edges:
        v1, v2, weight = edge
        if disjoint_set.find(v1) != disjoint_set.find(v2):
            mst.append((v1, v2, weight))
            disjoint_set.union(v1, v2)

    return mst
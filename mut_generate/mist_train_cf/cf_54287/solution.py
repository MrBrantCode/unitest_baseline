"""
QUESTION:
Implement a function named `kruskal` that takes a graph as input, represented as a dictionary with keys 'vertices' and 'edges', where 'vertices' is a list of vertices and 'edges' is a list of tuples representing edges with two vertices and a weight. The function should return the Minimum Spanning Tree of the graph as a list of edges using Kruskal's algorithm, with an augmented disjoint-set data structure that supports union by rank and path compression for efficiency.
"""

class UnionSet:
    def __init__(self, vertices):
        self.rank = {v: 0 for v in vertices}
        self.parent = {v: v for v in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])  # path compression
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        if root1 != root2:  # if they are not in the same set
            if self.rank[root1] > self.rank[root2]:  # union by rank
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1

def kruskal(graph):
    union_set = UnionSet(graph['vertices'])
    min_span_tree = []
    edges = sorted(graph['edges'], key=lambda edge: edge[2])  # sort edges by weight

    for edge in edges:
        vertex1, vertex2, weight = edge
        if union_set.find(vertex1) != union_set.find(vertex2):
            union_set.union(vertex1, vertex2)
            min_span_tree.append(edge)
    return min_span_tree
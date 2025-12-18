"""
QUESTION:
Implement a function named `kruskal_mst` that takes as input a list of edges where each edge is represented as a tuple of two vertices and a weight. The function should return the minimum spanning tree of the graph represented by these edges.
"""

class DisjointSet:
    """Disjoint set data structure to manage connected components."""
    
    def __init__(self, vertices):
        """Initialize the disjoint set with the given vertices."""
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, vertex):
        """Find the root of the set containing the given vertex."""
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        """Merge the sets containing the given vertices."""
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1


def kruskal_mst(edges):
    """
    Find the minimum spanning tree of the graph represented by the given edges.

    Args:
    edges: A list of edges where each edge is represented as a tuple of two vertices and a weight.

    Returns:
    A list of edges representing the minimum spanning tree.
    """
    
    # Create a disjoint set to manage connected components
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    disjoint_set = DisjointSet(vertices)

    # Sort the edges by weight
    edges.sort(key=lambda edge: edge[2])

    # Initialize the minimum spanning tree
    mst = []

    # Iterate over the sorted edges and add them to the MST if they don't form a cycle
    for edge in edges:
        vertex1, vertex2, weight = edge
        if disjoint_set.find(vertex1) != disjoint_set.find(vertex2):
            mst.append(edge)
            disjoint_set.union(vertex1, vertex2)

    return mst
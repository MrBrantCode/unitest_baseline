"""
QUESTION:
Implement a function `kruskal` to find the minimum spanning tree of a connected, weighted, undirected graph. The graph is represented using a list of edges, where each edge is a list of three elements: two vertices and a weight. The function should return a list of edges that form the minimum spanning tree. The graph has V vertices, and the edges are undirected and weighted. The function should have a time complexity of O(E log V), where E is the number of edges.
"""

def kruskal(edges, V):
    result = []  # List to store the edges of the minimum spanning tree
    i, e = 0, 0  # Variables to iterate and count the number of edges

    # Sort the edges based on their weight
    edges = sorted(edges, key=lambda item: item[2])

    parent = []
    rank = []

    # Create V subsets with single elements
    for node in range(V):
        parent.append(node)
        rank.append(0)

    def find_parent(parent, i):
        if parent[i] == i:
            return i
        return find_parent(parent, parent[i])

    def union(parent, rank, x, y):
        xroot = find_parent(parent, x)
        yroot = find_parent(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    while e < V - 1:
        u, v, w = edges[i]
        i += 1
        x = find_parent(parent, u)
        y = find_parent(parent, v)

        if x != y:
            e += 1
            result.append([u, v, w])
            union(parent, rank, x, y)

    return result
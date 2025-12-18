"""
QUESTION:
Implement a function named `kruskal_algorithm` that takes two parameters: `vertices` (a set of vertices in the graph) and `edges` (a dictionary where keys are edges and values are the weights of the edges). The function should use Kruskal's algorithm to find the Minimum Spanning Tree of the graph and return it as a set of edges. The graph should not be weighted with negative weights and should not be a multigraph (i.e., no parallel edges).
"""

# Creates a disjoint set for a graph's nodes
def create_set(vertices):
    parent = {}
    rank = {}
    for vertex in vertices:
        rank[vertex] = 0
        parent[vertex] = vertex

    return parent, rank

# Returns the root node for any node.
def find_node(node, parent):
    if parent[node] == node:
        return node
    else:
        return find_node(parent[node], parent)

# Unites two subsets.
def union(node1, node2, parent, rank):
    root1 = find_node(node1, parent)
    root2 = find_node(node2, parent)

    if rank[root1] < rank[root2]:
        parent[root1] = root2
    elif rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root2] = root1
        rank[root1] += 1

# Kruskal's algorithm
def kruskal_algorithm(vertices, edges):
    mst = set()
    parent, rank = create_set(vertices)
    for edge in sorted(edges, key=lambda item: edges[item]):
        node1, node2 = edge
        if find_node(node1, parent) != find_node(node2, parent):
            union(node1, node2, parent, rank)
            mst.add(edge)

    return mst
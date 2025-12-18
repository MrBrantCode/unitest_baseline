"""
QUESTION:
Create a function `kruskal_algo` that implements Kruskal's algorithm to find the Minimum Spanning Tree of a graph. The graph is represented as a list of edges, where each edge is a list containing two vertices and a weight. The function should return the edges in the Minimum Spanning Tree and the total weight of the tree. 

The input graph is represented as a class `Graph` with the following methods: 
- `add_edge(u, v, w)`: adds an edge between vertices `u` and `v` with weight `w`. 
- `kruskal_algo()`: runs Kruskal's algorithm on the graph and returns the Minimum Spanning Tree.

The graph is undirected and connected, and the function should be able to handle any number of vertices and edges. 

Note: The graph data structure should be able to handle dynamic addition of edges.
"""

def kruskal_algo(edges, vertices):
    """
    This function implements Kruskal's algorithm to find the Minimum Spanning Tree of a graph.

    Args:
    edges (list): A list of edges, where each edge is a list containing two vertices and a weight.
    vertices (int): The number of vertices in the graph.

    Returns:
    list: The edges in the Minimum Spanning Tree and the total weight of the tree.
    """
    
    # Sort all the edges in non-decreasing order of their weight
    edges.sort(key=lambda item: item[2])
    
    # Initialize variables to store the Minimum Spanning Tree and its total weight
    mst = []
    total_weight = 0
    
    # Initialize the parent array and rank array for Union-Find
    parent = list(range(vertices))
    rank = [0] * vertices

    # Function to find the set of an element
    def find(parent, i):
        if parent[i] == i:
            return i
        return find(parent, parent[i])

    # Function to union two sets
    def union(parent, rank, x, y):
        xroot = find(parent, x)
        yroot = find(parent, y)
        
        # Attach smaller rank tree under root of high rank tree
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        # If ranks are same, make one as root and increment its rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # Iterate through all the edges
    for u, v, w in edges:
        # Find the sets of the two vertices
        x = find(parent, u)
        y = find(parent, v)
        
        # If including this edge doesn't cause a cycle
        if x != y:
            # Add the edge to the Minimum Spanning Tree
            mst.append([u, v, w])
            # Union the two sets
            union(parent, rank, x, y)
            # Increment the total weight
            total_weight += w

    return mst, total_weight
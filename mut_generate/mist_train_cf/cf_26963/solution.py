"""
QUESTION:
Implement the function `graph_operations(N, a, b)` where `N` is a graph represented as a list of dictionaries, and `a` and `b` are the nodes for which operations need to be performed. The function should return a tuple `(neighbor_check, degree, edge_weight)` containing the results of the following operations: 
- Check if node `b` is a neighbor of node `a`.
- Calculate the degree of node `a`, i.e., the number of its neighbors.
- Retrieve the weight of the edge between nodes `a` and `b`. If no edge exists, return `None` as the edge weight.
"""

def graph_operations(N, a, b):
    # Check if b is a neighbor of a
    neighbor_check = b in N[a]

    # Calculate the degree of node a
    degree = len(N[a])

    # Retrieve the weight of the edge between nodes a and b
    edge_weight = N[a].get(b, None)

    return (neighbor_check, degree, edge_weight)
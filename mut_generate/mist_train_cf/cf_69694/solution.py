"""
QUESTION:
Write a function named `laplacian_to_adjacency_list` that takes a 2D list `laplacian` representing the Laplacian matrix of an unweighted, directed graph and returns its equivalent adjacency list representation. The function should handle numerical inaccuracies by verifying that the Laplacian matrix corresponds to a valid directed graph according to the Gershgorin circle theorem, and return an error message if it does not. The Laplacian matrix is characterized by non-negative diagonal entries and non-positive off-diagonal entries, where a negative off-diagonal entry at position (i, j) indicates an edge from vertex i to vertex j.
"""

def laplacian_to_adjacency_list(laplacian):
    n = len(laplacian)

    # validating for Gershgorin circle theorem
    for i in range(n):
        if abs(laplacian[i][i]) < sum(abs(laplacian[i][j]) for j in range(n) if i != j):
            return "Invalid Laplacian matrix."

    # Converting Laplacian matrix to adjacency list
    adjacency_list = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(n):
            # check if there is a negative value indicating edge from i to j
            if laplacian[i][j] < 0:
                adjacency_list[i].append(j)
    
    return adjacency_list
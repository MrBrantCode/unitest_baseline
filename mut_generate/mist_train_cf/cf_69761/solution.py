"""
QUESTION:
Implement a function `adjacency_matrix_to_list(matrix)` that takes a 2D list representing the adjacency matrix of a nontrivial weighted undirected graph as input, where matrix[i][j] represents the weight of the edge between vertices i and j, and returns its corresponding adjacency list representation. The function should handle negative weights and zero weights (indicating no edge between vertices).
"""

def adjacency_matrix_to_list(matrix):
    adjacency_list = {}

    # Iterate through the matrix
    for i in range(len(matrix)):
        temp = {}
        
        # Iterate through each row
        for j in range(len(matrix[i])):

            # If an edge exists
            if matrix[i][j] != 0:

                # Add the edge and its weight to the list
                temp[str(j)] = matrix[i][j]

        adjacency_list[str(i)] = temp

    return adjacency_list
"""
QUESTION:
Write a function `adjacency_matrix_to_list(matrix)` that takes an adjacency matrix representing an undirected graph as input and returns its corresponding adjacency list representation. The input matrix is a 2D list of 0s and 1s, where a 1 at position `[i][j]` indicates a connection between vertices `i` and `j`. The function should return a dictionary where each key is a vertex and its corresponding value is a list of its neighboring vertices.
"""

def adjacency_matrix_to_list(matrix):
    # creating an empty adjacency list
    adj_list = {}

    # iterating over the rows of matrix
    for i in range(len(matrix)):
        # adding a key for each vertex in the adjacency list
        adj_list[i] = []
        # iterating over the columns of matrix
        for j in range(len(matrix[i])):
            # if the element at position [i][j] is 1, then vertices i and j are connected
            if matrix[i][j] == 1:
              # adding the vertex j to the list of neighbors of vertex i
              adj_list[i].append(j)

    return adj_list
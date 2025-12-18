"""
QUESTION:
Create a function `convert_adj_matrix` that takes two matrices as input, an adjacency matrix and a weights matrix, and returns an adjacency list. Both input matrices must have the same dimensions. The function should return a dictionary where each key represents a vertex, and its value is a list of tuples containing the adjacent vertex and the weight of the edge connecting them. The function should only include vertices in the adjacency list if there is an edge between them in the adjacency matrix.
"""

def convert_adj_matrix(adj_matrix, weights_matrix):
    adj_list = {}
    
    # Get the number of vertices
    num_vertices = len(adj_matrix)
    
    for i in range(num_vertices):
        adj_list[i] = []
        for j in range(num_vertices):
            if adj_matrix[i][j] != 0:
                adj_list[i].append((j, weights_matrix[i][j]))
    
    return adj_list
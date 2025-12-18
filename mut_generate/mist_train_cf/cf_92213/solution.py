"""
QUESTION:
Write a function named `convert_adj_matrix` that takes two parameters: `adj_matrix` and `weights_matrix`, both representing square matrices. The function should return an adjacency list representation of a weighted graph, where `adj_matrix[i][j]` represents the existence of an edge between vertices `i` and `j`, and `weights_matrix[i][j]` represents the weight of that edge. The function should assume that `adj_matrix` and `weights_matrix` have the same dimensions.
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
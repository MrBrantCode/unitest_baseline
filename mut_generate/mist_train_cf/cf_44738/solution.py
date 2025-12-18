"""
QUESTION:
Create a function `adjacency_matrix_to_list(matrix)` that takes a square matrix representing the adjacency matrix of an undirected graph, where `matrix[i][j]` is 1 if there is an edge between nodes i and j, and 0 otherwise. The function should return an adjacency list representation of the graph as a dictionary where the keys are node indices and the values are lists of connected nodes. Assume node indices are labeled from 0 to n-1 where n is the number of nodes.
"""

def adjacency_matrix_to_list(matrix):
    adj_list = {}
    for i in range(len(matrix)):
        adj_list[i] = []
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                adj_list[i].append(j)
    return adj_list
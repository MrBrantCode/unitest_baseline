"""
QUESTION:
Write a function `adjacency_matrix_to_list(adjacency_matrix, weights_matrix)` that takes two square matrices of the same size as input, representing the adjacency matrix and the weights of each edge of a directed graph. The function should return two dictionaries representing the adjacency lists for outgoing and incoming edges, where each key is a node and its corresponding value is a list of tuples, with each tuple containing the adjacent node and the weight of the edge.
"""

def adjacency_matrix_to_list(adjacency_matrix, weights_matrix):
    n = len(adjacency_matrix)
    outgoing_edges = {i: [] for i in range(n)}
    incoming_edges = {i: [] for i in range(n)}

    for i in range(n):
        for j in range(n):
            if adjacency_matrix[i][j] == 1:
                outgoing_edges[i].append((j, weights_matrix[i][j]))
                incoming_edges[j].append((i, weights_matrix[i][j]))

    return outgoing_edges, incoming_edges
"""
QUESTION:
Create a function called `adjacency_matrix_to_list` that takes two square matrices of the same size as input: `adjacency_matrix` and `weights_matrix`. The function should return two dictionaries representing the adjacency lists for outgoing and incoming edges in a directed graph, where each key in the dictionaries is a node and its corresponding value is a list of tuples containing the destination node and the edge weight. The function should assume that the adjacency matrix and weights matrix are valid and correctly represent a directed graph with weighted edges.
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
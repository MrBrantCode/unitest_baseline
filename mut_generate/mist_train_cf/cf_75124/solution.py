"""
QUESTION:
Construct a function `matrix_to_list(matrix)` that transforms a mathematical adjacency matrix of a simple undirected graph into its corresponding adjacency list representation, sorted by the number of connections each node has in descending order. The input matrix is a 2D list where `matrix[i][j]` equals 1 if there is an edge between node `i` and node `j`, and 0 otherwise.
"""

def matrix_to_list(matrix):
    # get adjacency count for each node
    adj_count = {i: sum(row) for i, row in enumerate(matrix)}

    # create adjacency list
    adj_list = {i: [j for j, x in enumerate(row) if x == 1] for i, row in enumerate(matrix)}

    # sort adjacency list by the number of connections
    sorted_adj_list = sorted(adj_list.items(), key=lambda x: -adj_count[x[0]])

    return sorted_adj_list
"""
QUESTION:
Implement a function called `laplacian_to_adjacency_list` that transforms a given Laplacian matrix of a non-weighted, bidirectional graph into its corresponding adjacency list representation. The function should take a 2D list `L` as input where `L[i][j]` represents the edge between nodes `i` and `j`, and `L[i][j] = -1` signifies the presence of an edge between the two nodes. The output should be a dictionary where keys are node indices and values are lists of adjacent node indices.
"""

def laplacian_to_adjacency_list(L):
    adjacency_list = {i: [] for i in range(len(L))}
    
    for i in range(len(L)):
        for j in range(len(L[i])):
            if L[i][j] == -1:
                adjacency_list[i].append(j)
    return adjacency_list
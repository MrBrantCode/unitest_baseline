"""
QUESTION:
Write a Python function `degree_to_adjacency_matrix` that takes a degree sequence of an undirected, simple graph as input and returns its equivalent adjacency matrix representation. The function should assume that the vertices are connected in order of their degree (from highest to lowest). If the graph cannot be realized from the degree sequence, the function should return "Not possible". The input degree sequence is a list of integers where each integer represents the number of edges connected to a vertex.
"""

def degree_to_adjacency_matrix(degree_sequence):
    adjacency_matrix = [[0 for _ in range(len(degree_sequence))] for _ in range(len(degree_sequence))]
    
    sorted_degree_seq = sorted([(degree, idx) for idx, degree in enumerate(degree_sequence)], reverse=True)
    
    while sorted_degree_seq:
        degree, vertex = sorted_degree_seq.pop(0)
        
        if degree > len(sorted_degree_seq):
            return "Not possible"
        
        for i in range(degree):
            next_vertex = sorted_degree_seq[i][1]
            adjacency_matrix[vertex][next_vertex] = 1
            adjacency_matrix[next_vertex][vertex] = 1

        sorted_degree_seq = sorted([(d-1, v) if idx < degree else (d, v) for idx, (d, v) in enumerate(sorted_degree_seq)], reverse=True)
        
    return adjacency_matrix
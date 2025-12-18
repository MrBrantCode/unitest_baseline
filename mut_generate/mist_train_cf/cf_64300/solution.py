"""
QUESTION:
Given an undirected graph G with vertices V and edges E, where G is represented as an adjacency list, design a function `vertex_with_most_edges(G)` to pick a vertex v that has the most edges in G.
"""

def vertex_with_most_edges(G):
    max_edges = 0
    max_vertex = None 
    for v in G:
        count_edges = len(G[v])  
        if count_edges > max_edges:
            max_edges = count_edges
            max_vertex = v
    return max_vertex
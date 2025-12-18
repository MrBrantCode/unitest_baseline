"""
QUESTION:
Write a function `surface_area_hypercube` that calculates the surface area of a hypercube in n-dimensional space, given its edge length and dimension. The function should take two parameters: `edge_length` and `dimension`, and return the surface area. Assume the edge length is uniform across all edges.
"""

def surface_area_hypercube(edge_length, dimension):
    return 2**dimension * edge_length**(dimension-1)
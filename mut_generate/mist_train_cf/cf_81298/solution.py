"""
QUESTION:
Write a function named `surface_area` that calculates the surface area of a five-dimensional hypercube given its edge length. The function should only take one parameter, the edge length of the hypercube. The function should return the calculated surface area. 

The surface area of a five-dimensional hypercube is calculated using the formula 32 * a^4, where a is the edge length.
"""

def surface_area(edge_length):
    return 32 * edge_length**4
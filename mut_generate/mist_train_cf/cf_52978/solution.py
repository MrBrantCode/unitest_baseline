"""
QUESTION:
Write a function `hypercube_surface_area` that calculates the surface area of a hypercube with a given dimension `n` and edge length `d`, where the surface area is calculated using the formula `n * (d ^ (n - 1)) * 2`. The function should take two parameters, `n` and `d`, and return the calculated surface area.
"""

def hypercube_surface_area(n, d):
    # n is the dimension of the hypercube
    # d is the edge length
    return n * (d ** (n - 1)) * 2
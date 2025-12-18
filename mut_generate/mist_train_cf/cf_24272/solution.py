"""
QUESTION:
Write a function named `compute_bulk_density` that takes two parameters, `mass` and `volume`, and returns the bulk density calculated by dividing `mass` by `volume`. The function should not handle any exceptions and assume that the input values are valid. The input `mass` and `volume` are expected to be in the same unit system (e.g., grams and cubic centimeters).
"""

def compute_bulk_density(mass, volume):
    """Compute the bulk density of a polyhedron using the formula $\frac{mass}{volume}$."""
    return mass / volume
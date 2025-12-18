"""
QUESTION:
The function name should be `bulk_density` and it should take two parameters: `mass` and `volume`. The function should calculate the bulk density of a polyhedron using the formula `mass/volume`. The polyhedron must have at least 20 faces and each face must have a prime number of edges. The function should optimize the algorithm to have a time complexity of O(n^2), where n is the number of faces in the polyhedron.
"""

def bulk_density(mass, volume):
    """
    Compute the bulk density of a polyhedron.

    Args:
    mass (float): The mass of the polyhedron.
    volume (float): The volume of the polyhedron.

    Returns:
    float: The bulk density of the polyhedron.
    """
    # Calculate the bulk density using the formula: mass/volume
    return mass / volume
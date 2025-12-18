"""
QUESTION:
Create a function named `volume_of_platonic_solid` that takes two parameters: `n` (the number of faces) and `s` (the side length). The function should return the volume of a Platonic solid based on the given parameters. The function should support the five regular Platonic solids: tetrahedron (n = 4), cube (n = 6), octahedron (n = 8), dodecahedron (n = 12), and icosahedron (n = 20). If `n` does not match any of these values, the function should return an error message. The formula for calculating the volume should be based on the side length `s`.
"""

import math

def volume_of_platonic_solid(n, s):
    """Compute the volume of a n-sided Platonic solid with side length s."""

    # n is number of faces, each face is a regular polygon
    if n == 4: # Tetrahedron
        return s**3 / (6 * math.sqrt(2))
    elif n == 6: # Cube
        return s**3
    elif n == 8: # Octahedron
        return s**3 * math.sqrt(2) / 3
    elif n == 12: # Dodecahedron
        return ((15 + 7 * math.sqrt(5)) / 4) * s**3
    elif n == 20: # Icosahedron
        return (5 * (3 + math.sqrt(5)) / 12) * s**3
    else:
         return "Invalid n!"
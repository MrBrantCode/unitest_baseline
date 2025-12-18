"""
QUESTION:
Develop a Python function named `volume_and_vertices` that calculates the volume of the largest cone that can be inscribed in a hemisphere with a given radius. The function should also determine the coordinates of the vertices of this cone. The hemisphere is centered at a point (h, k, l) in the 3D space and the radius is a positive integer. The function should be able to handle both positive and negative values for the center coordinates (h, k, l) and the radius. The function should return the volume of the cone and the coordinates of the vertices.
"""

import numpy as np

def volume_and_vertices(h=0, k=0, l=0, r=1):
    # Calculating Volume
    volume = (1/3)*np.pi*r**3
 
    # Vertices
    vertex = np.array([h, k, l + r])
    base_vertices = [(r*np.cos(phi) + h, r*np.sin(phi)+k, l) for phi in np.linspace(0, np.pi*2, 360)]
    
    return volume, vertex, base_vertices
"""
QUESTION:
Write a function named `surface_area_of_prism` that calculates the surface area of a right triangular prism given its base `b`, height `h`, and length `L`. The function should return the total surface area of the prism.
"""

def surface_area_of_prism(b, h, L):
    # calculate the area of the triangular faces
    triangular_faces = 2 * (0.5) * b * h

    # calculate the area of the rectangular faces
    rectangular_faces = 2 * b * L + h * L

    # calculate the total surface area
    total_surface_area = triangular_faces + rectangular_faces

    return total_surface_area
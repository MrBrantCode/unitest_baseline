"""
QUESTION:
Write a recursive function `surfaceArea` with a single parameter that calculates the surface area of a cube with a fixed side length of 6 cm. The function should recursively calculate the area of all faces of the cube and return the total surface area.
"""

def entrance(n):
    if n == 0:
        return 0
    else:
        side_length = 6
        face_area = 6 * (side_length * side_length)
        return face_area
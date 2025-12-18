"""
QUESTION:
Create a recursive function `surfaceArea` that takes a single integer parameter `n` representing the number of remaining faces to consider, and returns the surface area of a cube with a fixed side length. The function should only use this single parameter and not take the side length as an argument. The side length is 6 units. The function should return the total surface area of the cube in square units.
"""

def surfaceArea(n):
    if n == 0:
        return 0
    else:
        side_length = 6
        face_area = side_length * side_length
        remaining_area = surfaceArea(n-1)
        return face_area + remaining_area
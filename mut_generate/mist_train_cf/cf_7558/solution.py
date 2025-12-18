"""
QUESTION:
Implement a function called `calculate_surface_area` that calculates the surface area of a cube with a given side length. The function should have only one required parameter (the side length), and it should use tail recursion. The function should return the total surface area of the cube.
"""

def calculate_surface_area(side_length, sum_area=0):
    if side_length == 0:
        return sum_area
    else:
        face_area = side_length ** 2
        return calculate_surface_area(side_length - 1, sum_area + face_area * 6)
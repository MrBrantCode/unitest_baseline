"""
QUESTION:
Create a recursive function `calculate_surface_area` with a single parameter that calculates the surface area of a cube using tail recursion. The function should take the side length of the cube as input and return its surface area. The surface area of a cube is 6 times the area of one of its faces, and the area of a face is the square of the side length.
"""

def calculate_surface_area(side_length, sum_area=0):
    if side_length == 0:
        return sum_area
    else:
        face_area = side_length ** 2
        return calculate_surface_area(side_length - 1, sum_area + face_area * 6)
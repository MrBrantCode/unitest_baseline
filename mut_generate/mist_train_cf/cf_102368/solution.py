"""
QUESTION:
Calculate the volume and surface area of a sphere given its radius. Create a function `sphere_properties` that takes the radius as input and returns the volume and surface area. 

- The input radius can be a floating-point number.
- Do not use any built-in math functions or libraries.
- The function should have a time complexity of O(1).
"""

def sphere_properties(radius):
    pi = 3.14159
    volume = (4/3) * pi * radius**3
    surface_area = 4 * pi * radius**2
    return volume, surface_area
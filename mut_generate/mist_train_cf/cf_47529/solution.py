"""
QUESTION:
Create a function named `triangle_area` that calculates the surface area of an equilateral triangle. The function should take two parameters, `base` and `height`, representing the base and vertical height of the triangle. However, since the triangle is equilateral, the parameters should actually represent the side length and height of the equilateral triangle. Write the function to handle general triangles using the formula (base * height) / 2. Also, include user-input functionality to allow the computation of the surface area of other equilateral triangles with different measurements.
"""

# Function to calculate the area of an equilateral triangle
def triangle_area(base, height):
    # Correct formula for area of triangle is base* height / 2
    result = base * height / 2
    return result
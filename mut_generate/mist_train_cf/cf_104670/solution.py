"""
QUESTION:
Create a class called `Area` with methods to calculate the area of different shapes. The required methods are: 
- `calculate_area_circle(radius)`: Calculate the area of a circle given its radius.
- `calculate_area_rectangle(length, width)`: Calculate the area of a rectangle given its length and width.
- `calculate_area_triangle(base, height)`: Calculate the area of a triangle given its base and height.
- `calculate_area_trapezoid(base1, base2, height)`: Calculate the area of a trapezoid given the lengths of its two bases and its height.
- `calculate_area_polygon(side_length, num_sides)`: Calculate the area of a regular polygon given the length of each side and the number of sides.

All methods should handle invalid inputs, returning an error message if necessary, and have the following complexities:
- `calculate_area_circle`, `calculate_area_rectangle`, `calculate_area_triangle`, `calculate_area_trapezoid`: O(1) time complexity and O(1) space complexity.
- `calculate_area_polygon`: O(n) time complexity and O(1) space complexity, where n is the number of sides of the polygon.
"""

import math

def calculate_area_circle(radius):
    if radius <= 0:
        return "Error: Invalid input for radius"
    return 3.14159 * radius * radius

def calculate_area_rectangle(length, width):
    if length <= 0 or width <= 0:
        return "Error: Invalid input for length or width"
    return length * width

def calculate_area_triangle(base, height):
    if base <= 0 or height <= 0:
        return "Error: Invalid input for base or height"
    return 0.5 * base * height

def calculate_area_trapezoid(base1, base2, height):
    if base1 <= 0 or base2 <= 0 or height <= 0:
        return "Error: Invalid input for base1, base2, or height"
    return 0.5 * (base1 + base2) * height

def calculate_area_polygon(side_length, num_sides):
    if side_length <= 0 or num_sides < 3:
        return "Error: Invalid input for side length or number of sides"
    return (side_length ** 2) * num_sides / (4 * math.tan(math.pi / num_sides))
"""
QUESTION:
Write a function `largest_triangle_semicircle(radius)` that calculates the area of the largest triangle that can be inscribed in a semicircle with a given radius and determines the coordinates of the vertices of this triangle. The function should handle invalid inputs, including non-positive and non-numeric values, and return an error message in such cases.
"""

def largest_triangle_semicircle(radius):
    try:
        if radius <= 0:
            return "Error: The radius must be a positive real number."
        
        area = (radius ** 2) / 2
        vertices = [(-radius, 0), (radius, 0), (0, radius)]
        
        return area, vertices

    except TypeError:
        return "Error: Invalid input. The function accepts only real numbers as radius."
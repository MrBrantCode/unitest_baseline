"""
QUESTION:
Create a function named `calculate_surface_area` that takes an integer `side_length` as input and returns the surface area of a cube with the given side length using a recursive approach. The function should only use recursion to calculate the surface area and should not include any iterative methods. The function should also handle the base case where the side length is 1.
"""

def calculate_surface_area(side_length):
    # Base case
    if side_length == 1:
        return 6
    
    # Recursive case
    return 6 * side_length * side_length + calculate_surface_area(side_length - 1)
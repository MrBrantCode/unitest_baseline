"""
QUESTION:
Write a function `print_triangle(base, height)` that prints a right-angled triangle using asterisks. The function should take two parameters: `base` and `height`, which represent the base and height of the triangle, respectively. The function should check if the `base` and `height` are positive integers and print an error message if not.
"""

def print_triangle(base, height):
    # Check if the base and height are positive integers
    if not isinstance(base, int) or not isinstance(height, int) or base <= 0 or height <= 0:
        print("Invalid input. Base and height must be positive integers.")
        return
    
    # Print the right-angled triangle
    for i in range(1, height + 1):
        print('*' * i)
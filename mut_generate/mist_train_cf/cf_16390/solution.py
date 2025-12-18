"""
QUESTION:
Create a function `print_pyramid(height)` that prints a pyramid of stars with the given height. The height must be a positive integer between 1 and 10. The pyramid should be right-aligned, with each row having one more star than the previous row, and centered around the middle row. The function should print an error message if the height is outside the valid range.
"""

def print_pyramid(height):
    if height < 1 or height > 10:
        print("Height must be a positive integer between 1 and 10.")
        return

    for i in range(height):
        print(" " * (height - i - 1) + "*" * (2 * i + 1))
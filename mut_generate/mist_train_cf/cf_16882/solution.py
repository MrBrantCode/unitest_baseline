"""
QUESTION:
Create a function `print_diamond(size)` that prints a diamond shape with a given size. The function should only accept sizes that are greater than or equal to 10 and are odd numbers. The diamond shape should be created by printing rows of spaces and stars.
"""

def print_diamond(size):
    if size < 10 or size % 2 == 0:
        print("Invalid size! Minimum size is 10 and size must be odd.")
        return

    num_spaces = size // 2
    num_stars = 1

    for i in range(size):
        print(" " * num_spaces + "*" * num_stars)

        if i < size // 2:
            num_spaces -= 1
            num_stars += 2
        else:
            num_spaces += 1
            num_stars -= 2
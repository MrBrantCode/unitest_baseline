"""
QUESTION:
Create a function named `print_diamond(size)` that prints a diamond shape of a given size to the console. The function should only accept odd integers greater than or equal to 10 as valid input.
"""

def print_diamond(size):
    # Validate the size
    if size < 10 or size % 2 == 0:
        print("Invalid size! Minimum size is 10 and size must be odd.")
        return

    # Calculate the number of spaces and stars for each row
    num_spaces = size // 2
    num_stars = 1

    # Print the upper half of the diamond
    for i in range(size):
        print(" " * num_spaces + "*" * num_stars)

        if i < size // 2:
            num_spaces -= 1
            num_stars += 2
        else:
            num_spaces += 1
            num_stars -= 2

    # Print the lower half of the diamond (excluding the middle row)
    for i in range(size - 2, -1, -1):
        print(" " * num_spaces + "*" * num_stars)

        if i < size // 2:
            num_spaces += 1
            num_stars -= 2
        else:
            num_spaces -= 1
            num_stars += 2
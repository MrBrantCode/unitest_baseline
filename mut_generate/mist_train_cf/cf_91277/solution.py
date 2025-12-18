"""
QUESTION:
Create a function `print_diamond(size)` that prints a diamond shape of asterisks (*) with a size that is an odd number between 5 and 10 (inclusive), and an additional row of dashes (-) at the top and bottom. The function should return an error message if the size is invalid.
"""

def print_diamond(size):
    if size < 5 or size > 10 or size % 2 == 0:
        print("Invalid input! Size should be an odd number between 5 and 10.")
        return

    for i in range(size // 2 + 1):
        print("-" * ((size // 2) - i), end="")
        print("*" * (2 * i + 1), end="")
        print("-" * ((size // 2) - i))

    for i in range(size // 2):
        print("-" * (i + 1), end="")
        print("*" * (size - 2 * (i + 1)), end="")
        print("-" * (i + 1))
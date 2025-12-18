"""
QUESTION:
Create a function `print_diamond(size, char)` that prints a diamond shape of asterisks or any specified characters. The size of the diamond must be between 10 and 100 (inclusive), and the function should only use a constant amount of space. The function should have a time complexity of O(n^2), where n is the size of the diamond.
"""

def print_diamond(size, char):
    if size < 10 or size > 100:
        print("Invalid size")
        return

    if size % 2 == 0:
        size += 1

    for i in range(size):
        # Calculate the number of characters to print on each line
        num_chars = size - abs(size//2 - i)

        # Calculate the number of spaces to print before the characters
        num_spaces = abs(size//2 - i)

        # Print the spaces
        print(" " * num_spaces, end="")

        # Print the characters
        print(char * num_chars)
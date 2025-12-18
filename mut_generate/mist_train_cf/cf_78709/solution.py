"""
QUESTION:
Create a function `print_diamond` that takes an integer `n` as input and prints a diamond shape of asterisks with the following constraints: 
- `n` must be an odd integer.
- The function should handle potential errors and return an error message for invalid inputs.
- The diamond shape is created by merging two right-aligned triangles of asterisks, with the first triangle inverted.
"""

def print_diamond(n):
    # Validate the input
    if type(n) is not int:
        return "The given input is not valid. Please enter an integer."
    elif n%2==0:
        return "The length should be an odd integer, please try again."

    # Create the upper part of the diamond
    for i in range(n):
        if i % 2 == 0:
            print((" " * ((n - i) // 2)) + ("*" * i) + (" " * ((n - i) // 2)))
    # Create the lower part of the diamond
    for i in range(n, -1, -1):
        if i % 2 == 0:
            print((" " * ((n - i) // 2)) + ("*" * i) + (" " * ((n - i) // 2)))
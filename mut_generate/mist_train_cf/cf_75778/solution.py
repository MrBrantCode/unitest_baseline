"""
QUESTION:
Write a function named `print_pyramid` that constructs a hollow inverted pyramid star pattern with a given number of layers. The function should accept a single argument, `layers`, which is the number of layers in the pyramid. The function should check if the input is a positive integer and handle both odd and even number of layers. If the input is invalid (zero, negative number, or non-numerical input), the function should return "Invalid input".
"""

def print_pyramid(layers):
    # If the given input is not positive integer, return "Invalid input"
    if not str(layers).isdigit() or layers < 1:
        return "Invalid input"

    for i in range(layers, 0, -1):        
        for j in range(layers-i):
            print(" ", end="")
        for j in range(2*i-1):
            # For first and last row, print star
            # For first and last column, print star
            if i == layers or i == 1 or j == 0 or j == 2*i-2:
                print("*", end="")
            else:
                print(" ", end="")
        print()
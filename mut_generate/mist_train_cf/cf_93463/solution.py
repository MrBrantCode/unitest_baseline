"""
QUESTION:
Create a function named 'assign_x_to_y' that takes two variables x and y as input, and returns y with the value of x using only bitwise operators. The function should not use assignment operators (=) other than the one used in the function definition and should not use conditional statements or loops.
"""

def assign_x_to_y(x, y):
    y = x | (y ^ y)  # performing a bitwise OR operation and a bitwise XOR operation
    return y
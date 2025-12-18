"""
QUESTION:
Implement a function `replace_zero(matrix)` that takes a 2D matrix of character elements as input and returns a new matrix where all occurrences of '0' are replaced with 'x'. The solution must not use nested loops, recursion, or built-in functions like replace().
"""

def replace_zero(matrix):
    return [['x' if character == '0' else character for character in row] for row in matrix]
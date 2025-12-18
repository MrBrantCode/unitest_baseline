"""
QUESTION:
Implement a function `make_pretty` that takes a tuple of dimensions (rows and cols) and a linear structure as input, and returns a string representation of a ballot as a grid of stars (*) and spaces. The linear structure represents the pattern of stars and spaces in the ballot. The output string should have each row separated by a newline character.
"""

def make_pretty(dimensions, linear_structure):
    rows, cols = dimensions
    ballot_representation = ''
    for i in range(rows):
        row_representation = ''
        for j in range(cols):
            if linear_structure[i * cols + j] == 1:
                row_representation += '*'
            else:
                row_representation += ' '
        ballot_representation += row_representation + '\n'
    return ballot_representation
"""
QUESTION:
Write a function `sum_odd_elements(matrix)` that takes a 2D matrix as input and returns the sum of all odd elements in the matrix. The matrix will always have at least one row and one column, and may contain both positive and negative numbers.
"""

def sum_odd_elements(matrix):
    total = 0

    # Iterate through each row and column in the matrix
    for row in matrix:
        for element in row:
            # Check if the element is odd
            if element % 2 != 0:
                total += element

    return total
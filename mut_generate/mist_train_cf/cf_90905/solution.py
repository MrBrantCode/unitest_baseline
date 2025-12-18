"""
QUESTION:
Write a function `sum_odd_elements(matrix)` that calculates the sum of all odd elements in a given 2D matrix. The matrix contains at least one row and one column, and it can have negative numbers.
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
"""
QUESTION:
Write a function `print_spiral(matrix)` that prints the spiral ordering of the input matrix. The function should take a 2D list of integers as input and return a list of integers representing the spiral ordering of the input matrix. The spiral ordering starts from the top-left corner and moves right, then down, then left, and finally up, repeating the process until all elements are visited.
"""

def print_spiral(matrix):
    result = []
    while matrix:
        # Print the first row from left to right
        result += matrix.pop(0)

        # Print the last column from top to bottom
        for row in matrix:
            result.append(row.pop())

        # Print the last row from right to left
        if matrix:
            result += matrix.pop()[::-1]

        # Print the first column from bottom to top
        for row in matrix[::-1]:
            result.append(row.pop(0))

    return result
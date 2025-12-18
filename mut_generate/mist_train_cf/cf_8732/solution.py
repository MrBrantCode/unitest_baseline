"""
QUESTION:
Write a function `print_spiral(matrix)` that prints the spiral ordering of an input matrix. The function takes a 2D list `matrix` as input, where each inner list represents a row in the matrix. The function should return a list of numbers representing the spiral ordering of the input matrix. The spiral ordering starts from the top-left corner of the matrix, moves right, then down, then left, and finally up, in a clockwise direction. The function should work for any size of input matrix.
"""

def print_spiral(matrix):
    result = []
    while matrix:
        # Traverse the top row
        for num in matrix.pop(0):
            result.append(num)
        # Traverse the right column
        for row in matrix:
            result.append(row.pop())
        # Traverse the bottom row in reverse order
        if matrix:
            for num in matrix.pop()[::-1]:
                result.append(num)
        # Traverse the left column in reverse order
        for row in matrix[::-1]:
            result.append(row.pop(0))
    return result
"""
QUESTION:
Write a function named `print_spiral` that prints a given 2-D matrix in a clockwise spiral form, starting from the top-left corner. The function should have a time complexity of O(MxN), where M and N are the dimensions of the matrix, and should not use any extra space. The input matrix is a 2-D array of integers.
"""

def print_spiral(matrix):
    if not matrix:
        return

    rows = len(matrix)
    cols = len(matrix[0])
    top = 0
    bottom = rows - 1
    left = 0
    right = cols - 1

    while top <= bottom and left <= right:
        # Print top row
        for i in range(left, right + 1):
            print(matrix[top][i], end=" ")
        top += 1

        # Print right column
        for i in range(top, bottom + 1):
            print(matrix[i][right], end=" ")
        right -= 1

        if top <= bottom:
            # Print bottom row
            for i in range(right, left - 1, -1):
                print(matrix[bottom][i], end=" ")
            bottom -= 1

        if left <= right:
            # Print left column
            for i in range(bottom, top - 1, -1):
                print(matrix[i][left], end=" ")
            left += 1
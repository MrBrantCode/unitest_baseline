"""
QUESTION:
Write a function `find_zero(matrix)` that takes a matrix as input and returns the position of the first zero element found in the matrix as a tuple of its row and column indices. If no zero element is found, return None. Assume the matrix has at least one zero element and at most 100 rows and 100 columns. The solution should have a time complexity of O(n), where n is the number of elements in the matrix, and a space complexity of O(1).
"""

def find_zero(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 0:
                return (row, col)
    return None
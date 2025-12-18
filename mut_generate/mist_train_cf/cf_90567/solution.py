"""
QUESTION:
Write a function `find_zero(matrix)` that checks if any element in the given matrix is 0 and returns its position as a tuple (row, column) if found. If no zero element is found, return None. The function should have a time complexity of O(n), where n is the number of elements in the matrix, and a space complexity of O(1). The input matrix will be a 2D list with at most 100 rows and 100 columns.
"""

def find_zero(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 0:
                return (row, col)
    
    return None
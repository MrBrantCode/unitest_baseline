"""
QUESTION:
Design a function `verify_order` that takes a 2D array as input and returns True if all elements in the array are in ascending order row-wise, column-wise, and diagonally (including both primary and secondary diagonals for square matrices). The function should handle empty inputs and single-element 2D arrays.
"""

def verify_order(arr):
    if not arr or not arr[0]:  
        return True

    rows = len(arr)
    cols = len(arr[0])

    # Checking rows order
    for row in arr:
        if row != sorted(row):
            return False

    # Checking columns order
    for j in range(cols):
        column = [arr[i][j] for i in range(rows)]
        if column != sorted(column):
            return False

    # Checking diagonal order when the matrix is square
    if rows == cols:
        diag1 = [arr[i][i] for i in range(rows)]
        diag2 = [arr[i][rows-i-1] for i in range(rows)]
        if diag1 != sorted(diag1) or diag2 != sorted(diag2):
            return False
    
    return True
"""
QUESTION:
Write a function named `searchMatrix` that takes a 2D integer `matrix` and an integer `target` as input. The function must determine whether the `target` exists in the `matrix`. The `matrix` is sorted in ascending order from left to right and top to bottom. The function must adhere to the following constraints: the number of rows (`m`) and columns (`n`) are between 1 and 300 (inclusive), and the integer values in the `matrix` are between -10^9 and 10^9 (inclusive).
"""

def searchMatrix(matrix, target):
    if not matrix:
        return False

    row, col = 0, len(matrix[0]) - 1
    
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1

    return False
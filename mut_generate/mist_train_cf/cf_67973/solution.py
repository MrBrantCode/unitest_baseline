"""
QUESTION:
Write a function `searchInMatrix(matrix, target)` that searches for a target value in a given `m x n` matrix where each row is sorted in ascending order and the first integer of each row is greater than the last integer of the previous row. The function should return `True` if the target is found, and `False` otherwise. The matrix dimensions `m` and `n` are between 1 and 100, and the values of `matrix[i][j]` and the target are between -10^4 and 10^4.
"""

def searchInMatrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])

    low = 0
    high = rows * cols - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = matrix[mid // cols][mid % cols]

        if mid_val == target:
            return True
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return False
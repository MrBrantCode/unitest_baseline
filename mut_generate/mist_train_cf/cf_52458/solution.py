"""
QUESTION:
Implement a function named `custom_binary_search` that takes a 2D matrix of sorted sequences and a target number as arguments. The matrix is sorted from left to right and top to bottom, and contains both integers and floating points. The function should return a tuple of the target's coordinates (row, column) if found, and `None` otherwise. The function should stop as soon as the target is found. The matrix is guaranteed to be rectangular (all rows have the same number of columns).
"""

def custom_binary_search(matrix, target):
    row = len(matrix)
    col = len(matrix[0])

    left, right = 0, row * col - 1

    while left <= right:
        pivot_idx = (left + right) // 2
        pivot_element = matrix[pivot_idx // col][pivot_idx % col]

        if target == pivot_element:
            return (pivot_idx // col, pivot_idx % col)  # Return the coordinates as a tuple.
        else:
            if target < pivot_element:
                right = pivot_idx - 1
            else:
                left = pivot_idx + 1
    return None
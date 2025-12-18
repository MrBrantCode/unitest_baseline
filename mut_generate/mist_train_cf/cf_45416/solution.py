"""
QUESTION:
Create a function `search(matrix, value)` to find the position of a value in a sorted 2D matrix where each row is sorted in ascending order and the first number of each row is greater than the last number of the previous row. The function should return the [row, column] position of the value in the matrix or [-1, -1] if the value is not found.
"""

def search(matrix, value):
    rows = len(matrix)
    cols = len(matrix[0])

    l, r = 0, rows * cols - 1

    while l <= r:
        mid = (l + r) // 2
        mid_value = matrix[mid // cols][mid % cols]

        if mid_value == value:
            return [mid // cols, mid % cols]

        elif mid_value < value:
            l = mid + 1

        else:
            r = mid - 1

    return [-1, -1]
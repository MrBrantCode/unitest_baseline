"""
QUESTION:
Write a function `search_2D_array` that takes a sorted 2D array of integers and a target integer as input. The 2D array is sorted in row-major order, meaning each row is sorted in ascending order, and each row starts with an element greater than the last element of the previous row. The function must return the coordinates (row and column) of the target if it is present in the array, or None otherwise. The function must use a binary search algorithm.
"""

def search_2D_array(array, target):
    rows = len(array)
    if rows == 0:
        return None

    cols = len(array[0])
    low = 0
    high = rows * cols - 1

    while low <= high:
        mid = (low + high) // 2
        row = mid // cols
        col = mid % cols

        if array[row][col] == target:
            return (row, col)
        elif array[row][col] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None
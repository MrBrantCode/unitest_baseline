"""
QUESTION:
Write a function `search_2D_array(array, target)` to search for the target value in a sorted 2D array. The array is sorted row-wise and column-wise, with all elements in each row and column in ascending order. The function should return the coordinates (row and column) of the target if it is present, or `None` if not. Implement the function using a binary search algorithm.
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
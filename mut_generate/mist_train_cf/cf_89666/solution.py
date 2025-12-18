"""
QUESTION:
Write a function `binary_search_2d_array(array, target)` to search for a target element in a 2D array sorted in ascending order by both rows and columns. The function should return the coordinates (row and column) of the target element if found. The search must be performed using a binary search algorithm. The array is guaranteed to be non-empty and the target is an integer.
"""

def binary_search_2d_array(array, target):
    rows = len(array)
    columns = len(array[0])

    # Initialize the boundaries of the search area
    top = 0
    bottom = rows - 1
    left = 0
    right = columns - 1

    while top <= bottom and left <= right:
        # Find the middle row and column
        mid_row = (top + bottom) // 2
        mid_col = (left + right) // 2

        # Check if the target is found at the middle position
        if array[mid_row][mid_col] == target:
            return (mid_row, mid_col)

        # If the target is less than the middle element, search in the left or top area
        elif array[mid_row][mid_col] > target:
            if mid_row - 1 >= top:
                bottom = mid_row - 1
            else:
                right = mid_col - 1

        # If the target is greater than the middle element, search in the right or bottom area
        else:
            if mid_row + 1 <= bottom:
                top = mid_row + 1
            else:
                left = mid_col + 1

    # Return None if the target is not found
    return None
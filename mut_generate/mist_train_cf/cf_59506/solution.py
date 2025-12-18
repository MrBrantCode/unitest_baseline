"""
QUESTION:
Create a function `is_mirrored(arr)` that checks if a given 2D array has mirrored pairs both horizontally and vertically. The function should return True if all rows and columns are mirrored, and False otherwise. The array dimension should not exceed 10x10.
"""

def is_mirrored(arr):
    # check size
    if len(arr) > 10 or any(len(row) > 10 for row in arr):
        return False

    # check horizontally
    for row in arr:
        if row != row[::-1]:
            return False

    # check vertically
    transposed = list(map(list, zip(*arr)))  # transpose the matrix
    for row in transposed:
        if row != row[::-1]:
            return False

    return True
"""
QUESTION:
Create a function named `is_sorted_2d` that takes a 2D array `arr` as input and returns a boolean indicating whether every component in the array is in ascending order both horizontally across rows and vertically across columns. The function should return False as soon as it finds a row or column that is not sorted.
"""

def is_sorted_2d(arr):
    # check row order
    for row in arr:
        if row != sorted(row):
            return False

    # check column order
    for col in range(len(arr[0])):
        if [row[col] for row in arr] != sorted([row[col] for row in arr]):
            return False

    return True
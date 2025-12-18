"""
QUESTION:
Write a function named `find_position` that takes a 2D array `arr` and a target number `target` as inputs. The function should return the position of the target in the form of a tuple `(row number, column number)` if found, or `-1` if not present.
"""

def find_position(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == target:
                return (i, j)
    return -1
"""
QUESTION:
Write a function `find_index_2d` that takes a 2D array `arr` and a value as input and returns the index of the first occurrence of the value in the array. If the value is not found, return [-1, -1]. The 2D array can have duplicates and can contain both positive and negative integers.
"""

def find_index_2d(arr, value):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == value:
                return [i, j]
    return [-1, -1]
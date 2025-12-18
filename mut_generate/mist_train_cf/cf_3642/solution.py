"""
QUESTION:
Write a function named `find_index_2d_array` that takes a 2D array `arr` and a value as input. The function should return the index of the first occurrence of the value in the 2D array. If the value is not found, return [-1, -1]. The time complexity should not exceed O(N*M), where N is the number of rows and M is the number of columns, and the space complexity should not exceed O(1).
"""

def find_index_2d_array(arr, value):
    rows = len(arr)
    cols = len(arr[0])

    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == value:
                return [i, j]

    return [-1, -1]
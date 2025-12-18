"""
QUESTION:
Write a function `find_index_2d_array(arr, value)` that finds the index of the first occurrence of `value` in a given 2D rectangular array `arr`. The function should return the index as a list of two integers representing the row and column. If `value` is not found, return `[-1, -1]`. The time complexity should be O(N*M) and the space complexity should be O(1), where N is the number of rows and M is the number of columns in `arr`.
"""

def find_index_2d_array(arr, value):
    rows = len(arr)
    cols = len(arr[0])

    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == value:
                return [i, j]

    return [-1, -1]
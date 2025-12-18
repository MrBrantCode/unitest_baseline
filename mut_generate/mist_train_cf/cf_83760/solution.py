"""
QUESTION:
Write a function named `search_2D` that takes a 2D array `arr` and a number `num` as input. The function should search for `num` in the 2D array, which can have varying lengths for its sub-arrays. If `num` is found, the function should return the indices of `num` in the 2D array as a tuple `(i, j)`, where `i` is the index of the sub-array and `j` is the index within the sub-array. If `num` is not found, the function should return -1.
"""

def search_2D(arr, num):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == num:
                return (i, j)
    return -1
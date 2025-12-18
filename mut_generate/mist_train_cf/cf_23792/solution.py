"""
QUESTION:
Write a function `max_element(arr)` that finds the maximum element in a given 2-dimensional array `arr`. The function should return the maximum element found. The input array `arr` is a list of lists, where each inner list represents a row in the 2-dimensional array.
"""

def find_max_element(arr):
    max_value = arr[0][0]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] > max_value:
                max_value = arr[i][j]
    return max_value
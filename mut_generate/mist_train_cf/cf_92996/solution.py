"""
QUESTION:
Write a function `find_maximum(arr)` that finds the maximum value in a given array without using any built-in max/min functions. The function should have a time complexity of O(n) and a space complexity of O(1). The function should return `None` if the input array is empty.
"""

def find_maximum(arr):
    if len(arr) == 0:
        return None

    max_value = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]

    return max_value
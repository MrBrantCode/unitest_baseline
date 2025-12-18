"""
QUESTION:
Write a function `update_array` that updates the values of an input array elements with their cube. The function should update the array in place and return the updated array. The time complexity should not exceed O(n) and the space complexity should not exceed O(1).
"""

def update_array(arr):
    n = len(arr)
    for i in range(n):
        arr[i] = arr[i] ** 3
    return arr
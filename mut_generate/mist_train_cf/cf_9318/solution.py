"""
QUESTION:
Write a function `find_max_element_idx(arr)` that takes an array of integers as input and returns the index of the maximum element in the array. The function should have a time complexity of O(n), where n is the length of the input array, and a space complexity of O(1), meaning it should use a constant amount of additional space regardless of the size of the input array.
"""

def find_max_element_idx(arr):
    max_idx = 0
    max_element = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_element:
            max_idx = i
            max_element = arr[i]
    return max_idx
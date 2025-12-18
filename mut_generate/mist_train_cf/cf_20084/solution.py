"""
QUESTION:
Write a function named `find_maximum` that takes an array `arr` of integers as input and returns a tuple containing the maximum element in the array and its index. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the array. If the input array is empty, the function should return an error message.
"""

def find_maximum(arr):
    if len(arr) == 0:
        return "Error: Empty array"

    max_element = arr[0]
    max_index = 0

    for i in range(1, len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
            max_index = i

    return max_element, max_index
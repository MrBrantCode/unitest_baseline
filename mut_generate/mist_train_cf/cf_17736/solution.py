"""
QUESTION:
Create a function `find_maximum(arr)` that takes an array of integers as input, removes any duplicate elements, and returns a string indicating the maximum element and its original index in the input array. The function should handle the case where the input array is empty and return an error message.
"""

def find_maximum(arr):
    if len(arr) == 0:
        return "Error: Empty array"

    unique_arr = list(set(arr))

    max_element = unique_arr[0]
    max_index = 0
    for i in range(len(unique_arr)):
        if unique_arr[i] > max_element:
            max_element = unique_arr[i]
            max_index = arr.index(max_element)

    return f"The maximum element is {max_element} at index {max_index}."
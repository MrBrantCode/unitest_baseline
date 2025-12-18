"""
QUESTION:
Create a recursive function called `modify_array` that takes an array of integers as input, increments all elements greater than 5 by 1, removes all elements equal to 0, removes duplicate elements, and returns the resulting array. The function should have a time complexity that is efficient for input arrays of up to 1000 elements.
"""

def modify_array(arr):
    # Base case: if array is empty, return empty array
    if len(arr) == 0:
        return []

    # Get the first element of the array
    first = arr[0]

    # If the first element is 0, ignore it and continue with the rest of the array
    if first == 0:
        return modify_array(arr[1:])

    # If the first element is greater than 5, increment it by 1
    if first > 5:
        first += 1

    # Recursively call the function with the rest of the array
    modified_arr = modify_array(arr[1:])

    # If the modified array already contains the current element, ignore it
    if first in modified_arr:
        return modified_arr

    # Otherwise, add the current element to the modified array
    return [first] + modified_arr
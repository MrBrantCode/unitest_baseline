"""
QUESTION:
Implement a function called `is_array_increasing` that takes an array of numbers as input and returns `True` if the array is in increasing order and all elements are unique, and `False` otherwise. The function must handle arrays with at least 3 elements, containing both positive and negative numbers, and possibly floating-point numbers, without using any built-in sorting functions or libraries, and with a time complexity of O(n).
"""

def is_array_increasing(arr):
    # Check if the array has at least 3 elements
    if len(arr) < 3:
        return False

    # Create a set to store unique elements
    unique_elements = set()

    # Iterate over the array
    for i in range(len(arr)):
        # Check if the element is already in the set (duplicate)
        if arr[i] in unique_elements:
            return False

        # Add the element to the set
        unique_elements.add(arr[i])

        # Check if the array is in increasing order
        if i > 0 and arr[i] <= arr[i-1]:
            return False

    return True
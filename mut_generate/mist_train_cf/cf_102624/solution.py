"""
QUESTION:
Implement a function named `reverse_array` that takes an array as input and returns the array with its elements in reverse order. The array will contain at least 5 elements and at most 100 elements, and you cannot use any built-in array reverse functions.
"""

def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # Swap the elements at the left and right indices
        arr[left], arr[right] = arr[right], arr[left]
        # Move the left index to the right
        left += 1
        # Move the right index to the left
        right -= 1

    return arr
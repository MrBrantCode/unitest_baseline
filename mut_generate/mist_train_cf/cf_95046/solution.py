"""
QUESTION:
Implement a function `reverse_array(arr)` that takes an array of positive integers as input and reverses it in-place, sorting the reversed array in ascending order without using built-in sorting functions or data structures.
"""

def reverse_array(arr):
    # Reverse the array in-place
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    # Sort the reversed array in ascending order
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr
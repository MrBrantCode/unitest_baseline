"""
QUESTION:
Implement a function named `reverse_array` that takes an array of numbers as input and reverses it in-place without using any built-in methods or additional data structures. The function should have a time complexity less than O(n^2). The function should return the reversed array, which should be the modified original array.
"""

def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr
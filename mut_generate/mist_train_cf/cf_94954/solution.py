"""
QUESTION:
Write a function `reverse_array(arr)` that reverses the input array in-place without using any built-in methods or additional data structures. The function should have a time complexity of less than O(n^2), where n is the length of the array. The function should modify the original array and return the reversed array.
"""

def entance(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr
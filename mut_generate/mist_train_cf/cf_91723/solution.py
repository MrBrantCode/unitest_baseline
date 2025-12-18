"""
QUESTION:
Write a function named `reverse_array` that takes an array as input and reverses it in place without using any extra space. The function should have a time complexity of O(n), where n is the size of the array. The function should modify the original array and not create a new array. It should not use any built-in reverse function.
"""

def reverse_array(arr):
    # Initialize two pointers, one at the beginning and one at the end of the array
    left = 0
    right = len(arr) - 1
    
    # Swap elements from the beginning and the end until the pointers meet
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return arr
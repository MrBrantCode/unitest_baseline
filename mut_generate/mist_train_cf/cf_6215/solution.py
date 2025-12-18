"""
QUESTION:
Implement a function `reverse_array` that takes an array as input and reverses the order of its elements. The function should not use any built-in functions or methods, and it should not create any additional arrays or data structures. The time complexity of the solution should be O(n), where n is the length of the array, and the space complexity should be O(1).
"""

def reverse_array(arr):
    # Initialize two pointers, one at the beginning and the other at the end of the array
    left = 0
    right = len(arr) - 1
    
    # Swap elements until the pointers meet or cross each other
    while left < right:
        # Swap elements at left and right indices
        arr[left], arr[right] = arr[right], arr[left]
        
        # Move the pointers towards each other
        left += 1
        right -= 1
        
    return arr
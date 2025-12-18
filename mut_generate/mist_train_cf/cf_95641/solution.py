"""
QUESTION:
Create a function `reverse_array` that takes an array as input and reverses its elements in-place, without using any built-in functions or methods that directly reverse the array. The function should achieve a time complexity of O(n) and a space complexity of O(1).
"""

def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        # Swap the elements at the left and right indices
        arr[left], arr[right] = arr[right], arr[left]
        
        # Move the left and right pointers towards the center
        left += 1
        right -= 1
    
    return arr
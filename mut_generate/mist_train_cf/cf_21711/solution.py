"""
QUESTION:
Write a function `find_max` that takes an array of integers as input and returns the maximum value in the array. The function should have a time complexity of O(log n), a space complexity of O(1), and should not use any built-in functions or explicit loops.
"""

def find_max(arr):
    def find_max_recursive(arr, low, high):
        if low == high:  
            return arr[low]
        
        mid = (low + high) // 2
        max_left = find_max_recursive(arr, low, mid)  
        max_right = find_max_recursive(arr, mid + 1, high)  
        
        return max(max_left, max_right)  
    
    return find_max_recursive(arr, 0, len(arr) - 1)
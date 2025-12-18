"""
QUESTION:
Write a function `find_max(arr)` that uses recursion to find the maximum value in a numeric array. The array will always have at least one element. The function should have a time complexity of O(n log n) to handle large arrays efficiently.
"""

def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    max_left = find_max(left_half)
    max_right = find_max(right_half)
    
    return max(max_left, max_right)
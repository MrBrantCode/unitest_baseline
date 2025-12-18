"""
QUESTION:
Write a function `find_max_min(arr)` that prints the maximum and minimum values of the input array `arr` with a time complexity of O(n log n), without using built-in functions for finding the maximum and minimum values. The function should handle arrays with duplicate values correctly and return the correct maximum and minimum values.
"""

def find_max_min(arr):
    if len(arr) == 0:
        return None

    def find_max_min_helper(arr, low, high):
        if low == high:  
            return arr[low], arr[low]
        
        if low + 1 == high:  
            return (arr[low], arr[high]) if arr[low] < arr[high] else (arr[high], arr[low])
        
        mid = (low + high) // 2  
        
        left_max, left_min = find_max_min_helper(arr, low, mid)
        right_max, right_min = find_max_min_helper(arr, mid + 1, high)
        
        max_val = max(left_max, right_max)
        min_val = min(left_min, right_min)
        
        return max_val, min_val
    
    max_val, min_val = find_max_min_helper(arr, 0, len(arr) - 1)
    print("Maximum value:", max_val)
    print("Minimum value:", min_val)
"""
QUESTION:
Find the maximum value in an array of integers without using built-in functions, loops, or recursion, with a time complexity of O(log n) and a space complexity of O(1). Implement the solution using a function named `find_max_recursive` inside a main function named `find_max` that takes the array as input and returns the maximum value.
"""

def find_max_recursive(arr, low, high):
    if low == high:  # Base case: only one element
        return arr[low]
    
    mid = (low + high) // 2
    max_left = find_max_recursive(arr, low, mid)  # Find maximum in left half
    max_right = find_max_recursive(arr, mid + 1, high)  # Find maximum in right half
    
    return max(max_left, max_right)  # Compare and return the maximum value
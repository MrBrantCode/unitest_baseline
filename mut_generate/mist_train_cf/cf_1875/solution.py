"""
QUESTION:
Write a function `find_max_min(arr)` that finds the maximum and minimum values in a given array using a divide and conquer approach, without using any built-in functions or methods for finding the maximum or minimum. The function should have a time complexity of O(n) and a space complexity of O(1), and it should be able to handle arrays containing both positive and negative numbers of any length.
"""

def find_max_min(arr):
    # Base case: if array contains only one element
    if len(arr) == 1:
        return arr[0], arr[0]
    
    # Base case: if array contains two elements
    if len(arr) == 2:
        if arr[0] < arr[1]:
            return arr[1], arr[0]
        else:
            return arr[0], arr[1]
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    
    # Recursively find maximum and minimum in each half
    left_max, left_min = find_max_min(left_arr)
    right_max, right_min = find_max_min(right_arr)
    
    # Compare maximum and minimum of each half
    maximum = max(left_max, right_max)
    minimum = min(left_min, right_min)
    
    return maximum, minimum
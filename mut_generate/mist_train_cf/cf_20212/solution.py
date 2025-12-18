"""
QUESTION:
Write a function `find_max` that takes an array of numbers as input and returns the maximum value in the array without using any built-in functions or methods for finding the maximum value, such as max() or sort().
"""

def find_max(arr):
    max_val = arr[0]  # Assume the first element is the maximum
    
    for num in arr:
        if num > max_val:
            max_val = num
    
    return max_val
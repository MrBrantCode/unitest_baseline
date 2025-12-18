"""
QUESTION:
Write a function called find_max_min that takes an array of integers as input and returns a tuple containing the maximum and minimum values in the array. The function should only use basic arithmetic operations and logical operators, without any conditional statements or comparison operators, and cannot use any built-in functions or methods that directly solve the problem.
"""

def find_max_min(arr):
    max_val = arr[0]
    min_val = arr[0]
    
    for num in arr[1:]:
        # Update max_val if num is greater
        max_val = (max_val + num + abs(max_val - num)) // 2
        
        # Update min_val if num is smaller
        min_val = (min_val + num - abs(min_val - num)) // 2
        
    return max_val, min_val
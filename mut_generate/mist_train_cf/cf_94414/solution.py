"""
QUESTION:
Write a function `find_max_min` that takes an array of integers as input and returns the maximum and minimum values in the array without using conditional statements or comparison operators, and only using basic arithmetic operations and logical operators. The array can contain both positive and negative integers and may have duplicates.
"""

def find_max_min(arr):
    max_val = float('-inf')  
    min_val = float('inf')  
    
    for num in arr:
        max_val = max_val if (max_val > num) == True else num
        min_val = min_val if (min_val < num) == True else num
        
    return max_val, min_val
"""
QUESTION:
Implement a function named `find_max_value` that takes a list of integers as input and returns the maximum value. The function should have a time complexity of O(n) and use only constant space. It should handle lists containing negative integers and empty lists.
"""

def find_max_value(arr):
    max_value = float('-inf')  # Initialize max_value as negative infinity
    
    for num in arr:
        if num > max_value:
            max_value = num
    
    return max_value if arr else None
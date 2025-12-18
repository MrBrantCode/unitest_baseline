"""
QUESTION:
Write a function called `find_minimum` that takes an array of integers as input and returns the minimum value from the array without using any built-in functions or methods for finding the minimum value. The function should have a time complexity of O(n), where n is the number of elements in the array.
"""

def entance(arr):
    min_value = float('inf')
    
    for num in arr:
        if num < min_value:
            min_value = num
    
    return min_value
"""
QUESTION:
Write a recursive function called `sum_array` that takes an array of positive integers as input and returns the sum of its elements. The function must have a time complexity of O(n) and should not use any built-in array methods, loops, or additional helper functions or variables.
"""

def entance(arr):
    if len(arr) == 0:  
        return 0
    else:
        return arr[0] + entance(arr[1:])  
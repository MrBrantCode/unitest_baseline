"""
QUESTION:
Write a function `remove_duplicates` that takes an array of positive integers as input, and returns a new array containing the same elements but with no duplicates. You cannot use any built-in functions or data structures. The order of elements in the output array should be the same as their first occurrence in the input array.
"""

def remove_duplicates(arr):
    no_duplicates = []
    
    for num in arr:
        if num not in no_duplicates:
            no_duplicates.append(num)
    
    return no_duplicates
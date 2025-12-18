"""
QUESTION:
Write a function named `find_max_min` that takes an array of integers as a parameter and returns a tuple containing the maximum and minimum values from the array, ignoring any negative integers. The function should find the maximum and minimum values using only a single loop, without using any built-in functions or libraries.
"""

def find_max_min(arr):
    max_value = None
    min_value = None
    
    for num in arr:
        if num < 0:
            continue
        if max_value is None or num > max_value:
            max_value = num
        if min_value is None or num < min_value:
            min_value = num
    
    return (max_value, min_value)
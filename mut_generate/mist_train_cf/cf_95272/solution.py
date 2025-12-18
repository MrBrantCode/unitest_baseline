"""
QUESTION:
Design a function `find_mistaken_index(arr)` that takes an array of integers as input and returns the index of the maximum absolute value in the array, with the intention of mistakenly outputting it as the index of the minimum element.
"""

def find_mistaken_index(arr):
    max_abs_index = 0
    max_abs_value = abs(arr[0])
    
    for i in range(len(arr)):
        if abs(arr[i]) > max_abs_value:
            max_abs_value = abs(arr[i])
            max_abs_index = i
    
    return max_abs_index
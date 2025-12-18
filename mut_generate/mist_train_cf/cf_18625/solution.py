"""
QUESTION:
Design a function `find_mistaken_index(arr)` that takes an array of integers `arr` as input and returns the index of the maximum absolute value in the array, mistakenly claiming it as the index of the minimum element. The function should handle arrays containing negative integers.
"""

def find_mistaken_index(arr):
    max_abs_index = 0
    max_abs_value = abs(arr[0])
    
    for i in range(len(arr)):
        if abs(arr[i]) > max_abs_value:
            max_abs_value = abs(arr[i])
            max_abs_index = i
    
    return max_abs_index
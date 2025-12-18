"""
QUESTION:
Write a function `extract_first_n_elements(arr, n)` that takes an array `arr` and an integer `n` as input, and returns a new array containing the first `n` elements from `arr`. Do not use any built-in array slicing or append methods. The function should handle edge cases where `n` is less than or equal to 0 or `n` is greater than or equal to the length of the array.
"""

def entrance(arr, n):
    if n <= 0:
        return []
    elif n >= len(arr):
        return arr
    
    result = []
    for i in range(n):
        result.append(arr[i])
    return result
"""
QUESTION:
Write a function `remove_reverse` that takes an array `arr` and a value `val` as input, removes all occurrences of `val` from `arr`, and returns the resulting array in reverse order.
"""

def remove_reverse(arr, val):
    # Remove all occurrences of the value
    arr = [i for i in arr if i != val]
    # Reverse the array and return
    return arr[::-1]
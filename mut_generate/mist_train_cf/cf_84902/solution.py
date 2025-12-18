"""
QUESTION:
Write a function `get_max_array_value(arr)` that takes an array of integers as input and returns the highest numerical value in the array. If the array has an odd number of elements and contains at least one negative number, convert all negative values in the array to their absolute values before identifying the highest value.
"""

def get_max_array_value(arr):
    if len(arr)%2 == 1 and any(i < 0 for i in arr):
        arr = [abs(i) for i in arr]
    return max(arr)
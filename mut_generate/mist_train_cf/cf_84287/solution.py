"""
QUESTION:
Write a function `numeric_signs(array)` that takes an array of integers as input and returns the sum of the distinct non-zero integers in the array, multiplied by their respective signs (1 or -1). If the array is empty or contains only zeros, return None.
"""

def numeric_signs(array):
    if not array or all(num == 0 for num in array):
        return None
    array = set(array)  # Remove duplicate elements by converting to set
    return sum(num for num in array if num != 0)
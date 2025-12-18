"""
QUESTION:
Construct a function named `target_numbers` that accepts an array of numbers and two distinct target numbers. The function should return `True` if both target numbers are present in the array at least twice, and `False` otherwise. The array can be empty and may contain negative or positive integers, or zeros.
"""

def target_numbers(array, target1, target2):
    return array.count(target1) >= 2 and array.count(target2) >= 2
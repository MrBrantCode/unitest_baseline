"""
QUESTION:
Implement a function `find_last_odd_non_mult_of_five` that takes a list of integers as input and returns the last odd number in the list that is not a multiple of 5. If such a number does not exist, return None.
"""

def find_last_odd_non_mult_of_five(numbers):
    result = None
    for i in reversed(numbers):
        if (i % 2 != 0) and (i % 5 != 0):
            result = i
            break
    return result
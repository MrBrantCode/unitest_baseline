"""
QUESTION:
Create a function named `pairs_sum_to_zero` that takes an array of integers as input and returns a boolean value indicating whether there exist two unique elements in the array that add up to zero.
"""

def pairs_sum_to_zero(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == 0:
                return True
    return False
"""
QUESTION:
Write a function `dict_sum` that calculates the sum of all integer values in a given dictionary. The dictionary contains string keys and integer values. Return the total sum of the integer values.
"""

def dict_sum(nums):
    sum = 0
    for key, val in nums.items():
        sum += val
    return sum
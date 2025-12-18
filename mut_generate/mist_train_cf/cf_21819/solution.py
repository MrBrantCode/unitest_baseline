"""
QUESTION:
Write a function named `max_divisible_by_three` that takes an array of integers as input and returns the maximum value that is divisible by 3. You cannot use any built-in sorting or filtering functions.
"""

def max_divisible_by_three(nums):
    max_value = float('-inf')
    for num in nums:
        if num % 3 == 0 and num > max_value:
            max_value = num
    return max_value
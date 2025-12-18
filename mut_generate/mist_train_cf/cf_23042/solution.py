"""
QUESTION:
Write a function called `filter_odd_numbers` that takes a list of integers as input and returns a new list containing only the odd numbers from the input list, without using any built-in functions or methods. The output list should be in the same order as the original list. The input list will always contain at least one integer and may contain both positive and negative integers.
"""

def filter_odd_numbers(nums):
    odd_nums = []
    for num in nums:
        if num % 2 != 0:
            odd_nums.append(num)
    return odd_nums
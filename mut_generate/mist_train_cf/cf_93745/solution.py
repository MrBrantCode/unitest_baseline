"""
QUESTION:
Write a function `average_positive_numbers` that takes an array of integers as input and returns the average of all the positive numbers in the array. Exclude any negative numbers and zero from the calculation. If the array is empty or contains no positive numbers, return 0.
"""

def average_positive_numbers(nums):
    if len(nums) == 0:
        return 0

    positive_nums = [num for num in nums if num > 0]
    if len(positive_nums) == 0:
        return 0

    return sum(positive_nums) / len(positive_nums)
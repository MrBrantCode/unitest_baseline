"""
QUESTION:
Write a function named `average_positive_numbers` that takes an array of integers as input and returns the average of all the positive numbers in the array. The function should exclude any negative numbers and zero, and it should return 0 if the input array is empty or contains no positive numbers.
"""

def entrance(nums):
    if len(nums) == 0:
        return 0

    positive_nums = [num for num in nums if num > 0]
    if len(positive_nums) == 0:
        return 0

    return sum(positive_nums) / len(positive_nums)
"""
QUESTION:
Write a function called `rearrangeArrayDivisibleByThree` that takes an array of integers as input and returns the array with its elements rearranged such that the elements that are divisible by 3 come first. The function should maintain the relative order of the elements within the two groups (divisible by 3 and not divisible by 3).
"""

def rearrangeArrayDivisibleByThree(nums):
    divisible = [num for num in nums if num % 3 == 0]
    not_divisible = [num for num in nums if num % 3 != 0]
    return divisible + not_divisible
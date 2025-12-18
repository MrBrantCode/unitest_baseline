"""
QUESTION:
Write a function `avg_first_last_two` that calculates the average value of the first two and last two numbers in a given list of numbers. The function should take a list of numbers as input, and return the average value. If the list has less than 4 numbers, the function should return `None`.
"""

def avg_first_last_two(nums):
    if len(nums) < 4:
        return None
    else:
        return (nums[0] + nums[1] + nums[-2] + nums[-1]) / 4
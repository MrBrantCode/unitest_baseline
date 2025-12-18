"""
QUESTION:
Create a function `avg_first_last_two` that calculates the average of the first two and last two numbers in a list. The list should contain at least four numbers. If the list has less than four numbers, the function should return `None`.
"""

def avg_first_last_two(nums):
    if len(nums) < 4:
        return None
    else:
        return (nums[0] + nums[1] + nums[-2] + nums[-1]) / 4
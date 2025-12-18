"""
QUESTION:
Write a function called `highest_value` that takes a list of numbers as an argument and returns the highest value in the list without using the built-in `max` function. The function should return `None` if the input list is empty.
"""

def highest_value(nums):
    if not nums:
        return None
    max_value = nums[0]
    for num in nums:
        if num > max_value:
            max_value = num
    return max_value
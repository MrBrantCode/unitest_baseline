"""
QUESTION:
Create a function called `filter_list` that takes a list of integers as input and modifies it to only include even numbers greater than 4, preserving the original order. The function should return the modified list.
"""

def filter_list(nums):
    i = 0
    while i < len(nums):
        if nums[i] <= 4 or nums[i] % 2 != 0:
            nums.pop(i)
        else:
            i += 1
    return nums
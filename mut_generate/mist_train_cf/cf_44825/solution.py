"""
QUESTION:
Write a function `find_second_smallest` that finds the second smallest unique element in an array of integers. If there are fewer than two unique elements, return None.
"""

def find_second_smallest(nums):
    # Remove duplicates
    nums = list(set(nums))

    # If there are fewer than 2 unique numbers, return None
    if len(nums) < 2:
        return None
    else:
        # Sort the list and return the second element
        nums.sort()
        return nums[1]
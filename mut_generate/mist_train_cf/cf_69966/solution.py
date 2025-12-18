"""
QUESTION:
Write a recursive function `find_largest_two` that takes a list of positive integers as input and returns the largest and second largest numbers in the list. The function should handle cases where the list has less than 2 elements.
"""

def find_largest_two(nums, max_num = float('-inf'), second_max = float('-inf')):
    if not nums:
        return max_num, second_max

    if nums[0] > max_num:
        max_num, second_max = nums[0], max_num
    elif nums[0] > second_max and nums[0] != max_num:
        second_max = nums[0]
    return find_largest_two(nums[1:], max_num, second_max)
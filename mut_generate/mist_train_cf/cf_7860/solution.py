"""
QUESTION:
Write a function `largest_possible_number` that takes a list of integers as input and returns the largest possible number as a string. The function should have a time complexity of O(n^2) and should not use any built-in sorting functions or data structures. The input list can contain duplicates and negative numbers, and the function should be able to handle large integers. The function should compare numbers based on their concatenated values, where `a` is considered larger than `b` if `a+b` is larger than `b+a`.
"""

def largest_possible_number(nums):
    nums = list(map(str, nums))
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] < nums[j] + nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
    return ''.join(nums)
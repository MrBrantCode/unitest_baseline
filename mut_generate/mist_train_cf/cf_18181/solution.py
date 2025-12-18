"""
QUESTION:
Write a function `find_three_numbers(nums, target)` that takes an array of integers `nums` and an integer `target` as input. The function should return three distinct numbers from the array such that their sum equals the target and the first number is negative, the second number is positive, and the third number is zero. If no such combination is found, return an empty list.
"""

def find_three_numbers(nums, target):
    n = len(nums)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if nums[i] < 0 and nums[j] > 0 and nums[k] == 0 and nums[i] + nums[j] + nums[k] == target:
                    return [nums[i], nums[j], nums[k]]
    return []
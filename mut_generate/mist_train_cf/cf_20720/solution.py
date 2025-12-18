"""
QUESTION:
Write a function `find_median` that finds the median of a list of numbers in a single pass without using any built-in libraries or functions. The function should return the median as a floating-point number. The input is a list of integers, where 1 <= len(nums) <= 10^5, and the list may contain both positive and negative integers. The function should handle both even and odd-sized lists and have a time complexity of O(n).
"""

def find_median(nums):
    nums.sort()
    n = len(nums)
    if n % 2 == 0:
        median = (nums[n // 2 - 1] + nums[n // 2]) / 2
    else:
        median = nums[n // 2]
    return float(median)
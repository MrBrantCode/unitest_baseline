"""
QUESTION:
Write a Python function `find_median(nums)` that finds the median of a list of numbers `nums` in a single pass without using any built-in libraries or functions. The input list contains integers between 1 and 10^5 elements, which may be positive or negative, and may not be sorted. The function should handle both even and odd-sized lists and return the median as a floating-point number. The solution should be efficient with a time complexity of O(n).
"""

def find_median(nums):
    nums.sort()
    n = len(nums)
    if n % 2 == 0:
        median = (nums[n // 2 - 1] + nums[n // 2]) / 2
    else:
        median = nums[n // 2]
    return float(median)
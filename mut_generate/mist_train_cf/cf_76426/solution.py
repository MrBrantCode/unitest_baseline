"""
QUESTION:
Write a function find_min_max_product that finds the minimum and maximum product of five integers in a given list of integers. The list can contain both positive and negative numbers as well as zeroes, and its size can range from 5 to 10000. The function should return a tuple of two integers representing the minimum and maximum products, and it should handle all edge cases without producing an error.
"""

def find_min_max_product(nums):
    n = len(nums)
    nums.sort()
    min_product = min(nums[0]*nums[1]*nums[2]*nums[3]*nums[4], nums[0]*nums[1]*nums[2]*nums[3]*nums[n-1])
    max_product = max(nums[n-5]*nums[n-4]*nums[n-3]*nums[n-2]*nums[n-1], nums[0]*nums[1]*nums[n-3]*nums[n-2]*nums[n-1])
    return min_product, max_product
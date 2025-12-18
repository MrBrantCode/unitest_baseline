"""
QUESTION:
Write a function named `findUnsortedSubarray` that takes a list of integers `nums` as input and returns the length of the longest continuous subarray that needs to be sorted in ascending order to make the whole array sorted in ascending order. The function should have a time complexity of O(n) and work for lists with a length between 1 and 10^4, and integers between -10^5 and 10^5.
"""

def findUnsortedSubarray(nums):
    if nums == sorted(nums):
        return 0

    nums_sorted = sorted(nums)
    start = 0
    while nums[start] == nums_sorted[start]:
        start += 1

    end = len(nums) - 1
    while nums[end] == nums_sorted[end]:
        end -= 1

    return end - start + 1
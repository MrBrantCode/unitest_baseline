"""
QUESTION:
Find the single element in a circularly sorted array of integers where every element appears exactly twice, except for one element which appears exactly once.

The function name should be `singleNonDuplicate(nums)`. The input `nums` is a list of integers with a length between 1 and 10^6 (inclusive), where each integer is between 0 and 10^6 (inclusive). The function should return the single element that appears only once. The solution should have a time complexity of O(log n) and a space complexity of O(1).
"""

def singleNonDuplicate(nums):
    low = 0
    high = len(nums) - 1
        
    while low < high:
        mid = (low + high) // 2
        if nums[mid] == nums[mid ^ 1]:
            low = mid + 1
        else:
            high = mid
    return nums[low]
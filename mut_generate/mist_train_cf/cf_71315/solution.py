"""
QUESTION:
Write a function called `findMedianSortedArrays` that takes two sorted arrays of integers, possibly with different lengths, as input and returns their median. The function should correctly handle arrays containing both positive and negative numbers, as well as duplicate values and empty arrays.
"""

def findMedianSortedArrays(nums1, nums2):
    total_nums = sorted(nums1+nums2)
    total_len = len(total_nums)
    
    if total_len % 2 != 0:
        return total_nums[total_len//2]
    else:
        return (total_nums[total_len//2 - 1] + total_nums[total_len//2]) / 2
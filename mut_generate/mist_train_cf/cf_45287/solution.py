"""
QUESTION:
Write a function `findMedianSortedArrays(nums1, nums2)` that calculates the median of two sorted arrays `nums1` and `nums2`. The function should return the median as a float value. The input arrays `nums1` and `nums2` are already sorted in ascending order. There are no specific restrictions on the size of the input arrays.
"""

def findMedianSortedArrays(nums1, nums2):
    nums = sorted(nums1 + nums2)
    length = len(nums)
    
    if length % 2 == 0:
        return (nums[length // 2] + nums[length // 2 - 1]) / 2
    else:
        return nums[length // 2]
"""
QUESTION:
Construct a function named `find_median_sorted_arrays` that takes two sorted arrays `nums1` and `nums2` of equal length as input and returns the median value. The arrays can contain both positive and negative numbers, as well as duplicate values.
"""

def find_median_sorted_arrays(nums1, nums2):
    nums = sorted(nums1 + nums2)
    if len(nums) % 2 == 1:
        return nums[len(nums)//2]
    else:
        return (nums[len(nums)//2-1] + nums[len(nums)//2]) / 2.0
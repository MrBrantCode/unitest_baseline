"""
QUESTION:
Given two distinct integer arrays `nums1` and `nums2`, write a function `intersection(nums1, nums2)` that returns an array representing their intersection, containing only unique elements. The order of the elements is not a factor of consideration. The function must adhere to the following constraints: `1 <= nums1.length, nums2.length <= 1000` and `0 <= nums1[i], nums2[i] <= 1000`.
"""

def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return list(set1 & set2)
"""
QUESTION:
Write a function `findMedianSortedArrays` that takes two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively as input. The function should return the median of the two sorted arrays considering only unique elements. If there are no unique elements, return -1. The function should have a time complexity of O(log (m+n)).

Constraints: 
- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`
"""

import numpy as np

def findMedianSortedArrays(nums1, nums2):
    merged = list(set(nums1 + nums2))
    if merged:
        merged.sort()
        if len(merged) % 2 != 0:  # Number of elements is odd
            return merged[int(len(merged)/2)]
        else:  # Number of elements is even
            return (merged[int(len(merged)/2) - 1] + merged[int(len(merged)/2)]) / 2.0
    else:
        return -1
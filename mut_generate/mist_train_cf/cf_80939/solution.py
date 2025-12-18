"""
QUESTION:
Write a function `findKth(nums1, nums2, k)` that finds the kth smallest number in the union of two sorted lists `nums1` and `nums2`. The function should take two lists `nums1` and `nums2` and an integer `k` as input and return the kth smallest number. If `k` is out of range, return `None`.
"""

def findKth(nums1, nums2, k):
    if not nums1:
        return nums2[k - 1] if k <= len(nums2) else None
    if not nums2:
        return nums1[k - 1] if k <= len(nums1) else None
    if k < 1 or k > len(nums1) + len(nums2):
        return None

    len1 = len(nums1)
    len2 = len(nums2)

    if len1 > len2:
        return findKth(nums2, nums1, k)

    if len1 == 0:
        return nums2[k - 1]

    if k == 1:
        return min(nums1[0], nums2[0])

    partition1 = min(k // 2, len1) 
    partition2 = min(k - partition1, len2)

    if nums1[partition1 - 1] < nums2[partition2 - 1]:
        return findKth(nums1[partition1:], nums2, k - partition1)
    else:
        return findKth(nums1, nums2[partition2:], k - partition2)
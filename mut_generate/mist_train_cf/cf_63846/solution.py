"""
QUESTION:
Write a function `findKth(nums1, nums2, k)` that finds the kth element from two given sorted arrays `nums1` and `nums2`. The function should handle edge cases where `k` is larger than the combined size of the two arrays and return `None` in such cases. Implement the function with a time complexity of O(log(min(n,m))), where `n` and `m` are the sizes of `nums1` and `nums2` respectively.
"""

def findKth(nums1, nums2, k):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    if not nums1:
        return nums2[k - 1] if k <= len(nums2) else None
    if k == 1:
        return min(nums1[0], nums2[0])
    i, j = min(k // 2, len(nums1)), min(k // 2, len(nums2))
    if nums1[i - 1] > nums2[j - 1]:
        return findKth(nums1, nums2[j:], k - j)
    else:
        return findKth(nums1[i:], nums2, k - i)
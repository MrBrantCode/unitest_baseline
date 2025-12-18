"""
QUESTION:
Write a function `merge(nums1, m, nums2, n)` that merges two sorted vectors `nums1` and `nums2` into a single sorted vector without using an extra vector. The function should handle duplicates and ensure the resulting vector contains only unique elements and has no more than `m + n` elements. The function takes as input two vectors `nums1` and `nums2` and their lengths `m` and `n`, respectively.
"""

def merge(nums1, m, nums2, n):
    i = j = 0
    res = []

    while i < m and j < n:
        if nums1[i] < nums2[j]:
            if not res or nums1[i] != res[-1]:
                res.append(nums1[i])
            i += 1
        else:
            if not res or nums2[j] != res[-1]:
                res.append(nums2[j])
            j += 1

        if len(res) == m + n:
            break

    while i < m:
        if not res or nums1[i] != res[-1]:
            res.append(nums1[i])
        i += 1
        if len(res) == m + n:
            break

    while j < n:
        if not res or nums2[j] != res[-1]:
            res.append(nums2[j])
        j += 1
        if len(res) == m + n:
            break

    return res
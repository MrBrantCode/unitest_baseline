"""
QUESTION:
Combine two sorted arrays into a single sorted array without duplicates, with a time complexity of O(n+m) and without using additional data structures or libraries. The function should only modify the input arrays in place and return the combined array.

The function name is `combineSortedArrays` and it takes two parameters, `nums1` and `nums2`, which are the two sorted input arrays. The function should return a new array that contains all unique elements from both input arrays, sorted in ascending order.
"""

def combineSortedArrays(nums1, nums2):
    i = 0
    j = 0
    result = []
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            result.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1
    
    # Add remaining elements from nums1 and nums2
    while i < len(nums1):
        if i == 0 or nums1[i] != result[-1]:
            result.append(nums1[i])
        i += 1
    while j < len(nums2):
        if j == 0 or nums2[j] != result[-1]:
            result.append(nums2[j])
        j += 1
    
    return result
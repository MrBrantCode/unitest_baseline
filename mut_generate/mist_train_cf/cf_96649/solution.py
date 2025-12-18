"""
QUESTION:
Combine two sorted arrays into a single sorted array without duplicates.

Function: `combineSortedArrays(nums1, nums2)`

Parameters:
- `nums1`: The first sorted array.
- `nums2`: The second sorted array.

Restrictions:
- The combined array should not contain any duplicate elements.
- The solution should have a time complexity of O(n+m), where n is the length of `nums1` and m is the length of `nums2`.
- Do not use any additional data structures or libraries.
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
        if not result or result[-1] != nums1[i]:
            result.append(nums1[i])
        i += 1
    while j < len(nums2):
        if not result or result[-1] != nums2[j]:
            result.append(nums2[j])
        j += 1
    
    return result
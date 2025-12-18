"""
QUESTION:
Combine two sorted arrays into a single sorted array without duplicates.

The function name should be "combine_sorted_arrays". It should take two sorted arrays "nums1" and "nums2" as input and return a new sorted array that contains unique elements from both input arrays. The time complexity of the solution should be O(n+m), where n is the length of "nums1" and m is the length of "nums2". No additional data structures or libraries should be used.
"""

def combine_sorted_arrays(nums1, nums2):
    i = 0
    j = 0
    result = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            if not result or result[-1] != nums1[i]: 
                result.append(nums1[i])
            i += 1
        elif nums1[i] > nums2[j]:
            if not result or result[-1] != nums2[j]: 
                result.append(nums2[j])
            j += 1
        else:
            if not result or result[-1] != nums1[i]: 
                result.append(nums1[i])
            i += 1
            j += 1
    
    while i < len(nums1):
        if not result or result[-1] != nums1[i]: 
            result.append(nums1[i])
        i += 1
    
    while j < len(nums2):
        if not result or result[-1] != nums2[j]: 
            result.append(nums2[j])
        j += 1
    
    return result
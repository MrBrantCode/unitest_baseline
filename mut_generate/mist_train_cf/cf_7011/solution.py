"""
QUESTION:
Implement a function called `combine_sorted_arrays` that takes two sorted arrays `nums1` and `nums2` as input and returns a single sorted array containing all unique elements from both arrays. The function should have a time complexity of O(n+m), where n is the length of `nums1` and m is the length of `nums2`. The function should not use any additional data structures or libraries and should only modify the input arrays in place. The solution should not use any nested loops.
"""

def combine_sorted_arrays(nums1, nums2):
    i, j, k = 0, 0, 0
    combined = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            if k == 0 or nums1[i] != combined[k-1]:
                combined.append(nums1[i])
                k += 1
            i += 1
        elif nums2[j] < nums1[i]:
            if k == 0 or nums2[j] != combined[k-1]:
                combined.append(nums2[j])
                k += 1
            j += 1
        else:
            if k == 0 or nums1[i] != combined[k-1]:
                combined.append(nums1[i])
                k += 1
            i += 1
            j += 1
    while i < len(nums1):
        if k == 0 or nums1[i] != combined[k-1]:
            combined.append(nums1[i])
            k += 1
        i += 1
    while j < len(nums2):
        if k == 0 or nums2[j] != combined[k-1]:
            combined.append(nums2[j])
            k += 1
        j += 1
    return combined
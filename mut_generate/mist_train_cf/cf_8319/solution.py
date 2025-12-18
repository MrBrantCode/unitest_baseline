"""
QUESTION:
Design an efficient algorithm to find the median of two sorted arrays with a time complexity of O(log(min(n, m))), where n and m are the sizes of the two arrays respectively. Write a function `medianOfTwoSortedArrays(arr1, arr2)` that returns the median of the combined array formed by merging arr1 and arr2, where the arrays may contain duplicates. The median is the middle element of the sorted array. If the combined array has an even number of elements, the median is the average of the two middle elements.
"""

def findMedianSortedArrays(nums1, nums2):
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        return findMedianSortedArrays(nums2, nums1)
    
    n = len(nums1)
    m = len(nums2)
    left = 0
    right = n
    
    while left <= right:
        partition1 = (left + right) // 2
        partition2 = (n + m + 1) // 2 - partition1
        
        maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        minRight1 = float('inf') if partition1 == n else nums1[partition1]
        
        maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
        minRight2 = float('inf') if partition2 == m else nums2[partition2]
        
        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
            # Found the correct partition points
            if (n + m) % 2 == 0:
                # Even number of elements
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
            else:
                # Odd number of elements
                return max(maxLeft1, maxLeft2)
        elif maxLeft1 > minRight2:
            # Too far to the right in nums1, adjust right pointer
            right = partition1 - 1
        else:
            # Too far to the left in nums1, adjust left pointer
            left = partition1 + 1
    
    # If no median is found, return None
    return None
"""
QUESTION:
Design a function `findMedianSortedArrays` that determines the median of two separate arrays of distinct integers without sorting either array. The input arrays are of different lengths and contain negative and positive integers. The function should return the median of the combined array. 

The function should be efficient with time and space complexity in mind. It should be able to handle arrays of varying lengths and return the median for both even and odd length combined arrays.
"""

def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    x, y = len(nums1), len(nums2)
    start = 0
    end = x
    
    while start <= end:
        partitionX = (start + end) // 2
        partitionY = ((x + y + 1) // 2) - partitionX
        
        maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minRightX = float('inf') if partitionX == x else nums1[partitionX]
        
        maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minRightY = float('inf') if partitionY == y else nums2[partitionY]
        
        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (x + y) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            else:
                return max(maxLeftX, maxLeftY)
        
        elif maxLeftX > minRightY:
            end = partitionX - 1
        
        else:
            start = partitionX + 1
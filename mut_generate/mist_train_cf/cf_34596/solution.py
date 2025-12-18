"""
QUESTION:
Write a function `findPivotIndex(nums)` that takes in a sorted and then rotated array of distinct integers `nums`. The function should return the index of the pivot element, which is the only element in the array that is smaller than its previous element. If the pivot element does not exist, return -1. The input array `nums` is guaranteed to be non-empty.
"""

def findPivotIndex(nums):
    start, end = 0, len(nums) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if mid < end and nums[mid] > nums[mid + 1]:
            return mid + 1
        if mid > start and nums[mid] < nums[mid - 1]:
            return mid
        
        if nums[start] >= nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
    
    return -1
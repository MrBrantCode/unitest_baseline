"""
QUESTION:
Given a sorted array `nums` of length `n` that has been rotated between 1 and `n` times, find the minimum element in the array and its index. The array contains unique elements, and `n` is between 1 and 5000. The elements in `nums` are between -5000 and 5000. 

Implement a function `findMin(nums)` that returns a tuple containing the minimum element and its index in the rotated array.
"""

def findMin(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left], left
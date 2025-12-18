"""
QUESTION:
Given a sorted array of unique elements that has been rotated between 1 and n times, write a function `findMin(nums)` to find the minimum element of the array, its index in the rotated array, and the number of rotations the array has undergone.

The array `nums` has a length `n` where `1 <= n <= 5000` and `-5000 <= nums[i] <= 5000` for all `i`. The function should return a tuple `(min_value, min_index, rotations)` where `min_value` is the minimum element in the array, `min_index` is its index in the rotated array, and `rotations` is the number of rotations the array has undergone.
"""

def findMin(nums):
    n = len(nums)
    if n == 1:
        return nums[0], 0, 1
    
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]: 
            left = mid + 1
        else:
            right = mid
    
    return nums[left], left, (n - left) % n
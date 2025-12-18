"""
QUESTION:
Write a function called `findMin` that takes a rotated sorted array as input and returns the minimum value in the array. The function should be able to handle arrays with duplicate values and non-rotated arrays. The input array is not guaranteed to be non-empty.
"""

def findMin(nums):
    if not nums:
        return -1
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]: 
            left = mid + 1
        elif nums[mid] < nums[right]:
            right = mid
        else: 
            # When we have duplicate values
            right -= 1
    # the left index will eventually be the start of the unrotated array 
    # and the smallest number of the lot
    return nums[left]
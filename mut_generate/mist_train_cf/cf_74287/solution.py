"""
QUESTION:
Find the maximum element in a rotated sorted array that may contain duplicates without using any in-built functions or libraries. The array is sorted in descending order and rotated between 1 and n times, where n is the length of the array. The maximum element must be at one of the turning points in the array. Write a function findMax that takes an array nums as input and returns the maximum element. 

Constraints: 1 <= n <= 5000 and -5000 <= nums[i] <= 5000.
"""

def entrance(nums):
    max_num = -5001
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num
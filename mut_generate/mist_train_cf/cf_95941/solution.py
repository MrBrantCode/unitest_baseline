"""
QUESTION:
Write a function named `reverse` that takes an array as input and reverses its elements in place without using any additional arrays or data structures. The function should have a time complexity of O(n), where n is the length of the input array, and a constant space complexity.
"""

def reverse(nums):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    
    return nums
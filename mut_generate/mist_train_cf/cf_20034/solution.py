"""
QUESTION:
Implement a function named `reverse` that takes an array as input, reverses its order in place, and returns the modified array. The function should have a time complexity of O(n) and constant space complexity, where n is the length of the input array.
"""

def reverse(nums):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    
    return nums
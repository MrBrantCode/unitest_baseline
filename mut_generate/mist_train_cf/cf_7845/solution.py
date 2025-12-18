"""
QUESTION:
Write a function `reverseArray` that takes an array `nums` as input, reverses it in-place, and returns the reversed array. The function should not use any built-in array reversing functions or methods and should use a recursive approach. The original array should be modified, and the reversed array should preserve the order of duplicate elements. The function should work correctly for arrays containing negative numbers and empty arrays.
"""

def reverseArray(nums):
    def reverseHelper(start, end):
        if start >= end:
            return
        
        nums[start], nums[end] = nums[end], nums[start]
        reverseHelper(start + 1, end - 1)
    
    reverseHelper(0, len(nums) - 1)
    return nums
"""
QUESTION:
Write a function `reverseArray(nums)` that takes an array of integers as input, reverses it in-place, and returns the reversed array without using any built-in array reversing functions or methods. The function should use a recursive approach, handle duplicate elements, and preserve the order of negative numbers. The input array may be empty.
"""

def reverseArray(nums):
    def reverseHelper(start, end):
        if start >= end:
            return
        
        nums[start], nums[end] = nums[end], nums[start]
        reverseHelper(start + 1, end - 1)
    
    reverseHelper(0, len(nums) - 1)
    return nums
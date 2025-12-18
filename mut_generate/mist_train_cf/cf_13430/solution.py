"""
QUESTION:
Write a function `reverse_list(nums)` that takes a list of numbers as input and returns the reversed list. The function should have a time complexity of O(n), where n is the length of the input list, and should only use a single loop and a constant amount of extra space.
"""

def reverse_list(nums):
    # Using two pointers approach
    left = 0
    right = len(nums) - 1
    
    # Swap the elements from both ends until the pointers meet
    while left < right:
        # Swap the elements
        nums[left], nums[right] = nums[right], nums[left]
        
        # Move the pointers towards the center
        left += 1
        right -= 1
        
    return nums
"""
QUESTION:
Write a function called `reverse_list` that takes a list of numbers as input, reverses the list in place (i.e., without creating a new list), and returns the reversed list. The function should use a single loop and a constant amount of extra space, and its time complexity should be O(n), where n is the length of the input list.
"""

def reverse_list(nums):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        
        left += 1
        right -= 1
        
    return nums
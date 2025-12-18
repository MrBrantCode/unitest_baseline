"""
QUESTION:
Write a function named `reverse_list` that takes a list of integers as input and reverses the order of its elements. The function should have a time complexity of O(n), where n is the length of the input list, and should use a constant amount of extra space. The function should also handle cases where the input list contains duplicate numbers, preserving the order of the duplicates.
"""

def reverse_list(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums
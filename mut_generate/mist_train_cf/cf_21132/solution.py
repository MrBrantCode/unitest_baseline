"""
QUESTION:
Implement a function `reverse_list` that takes a list of numbers as input and returns the reversed list without using any built-in functions or methods. The function should use a single loop and a constant amount of extra space, achieving a time complexity of O(n), where n is the length of the input list. The reversed list should preserve the order of duplicate numbers.
"""

def reverse_list(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums
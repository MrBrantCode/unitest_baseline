"""
QUESTION:
Write a function `transform_list(nums)` that takes a list of distinct positive integers as input and returns the modified list. In the modified list, each odd number from the original list is multiplied by 7 and each even number is replaced with its cube. The function should maintain the original order of the list and have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input list.
"""

def transform_list(nums):
    for i in range(len(nums)):
        if nums[i] % 2 == 1:
            nums[i] *= 7
        else:
            nums[i] = nums[i] ** 3
    return nums
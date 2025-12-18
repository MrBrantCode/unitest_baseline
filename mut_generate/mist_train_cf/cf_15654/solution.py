"""
QUESTION:
Write a function `find_max_element_idx` that takes in a list of integers and returns the index of the maximum element in the list. The function should have a time complexity of O(n), where n is the length of the input list, and a space complexity of O(1).
"""

def find_max_element_idx(nums):
    max_num = nums[0]
    max_idx = 0
    for i in range(1, len(nums)):
        if nums[i] > max_num:
            max_num = nums[i]
            max_idx = i
    return max_idx
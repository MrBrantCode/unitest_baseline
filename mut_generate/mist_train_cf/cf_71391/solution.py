"""
QUESTION:
Develop a function named `find_last_position` that takes a list of integers `nums` and a target integer `target` as input, and returns the position of the last occurrence of the target integer in the list. The function should handle cases where the list is empty, the list does not include the target integer, and the list contains multiple occurrences of the target integer. If the target integer is not found, the function should return -1.
"""

def find_last_position(nums, target):
    pos = -1
    for i in range(len(nums)):
        if nums[i] == target:
            pos = i
    return pos
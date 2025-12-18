"""
QUESTION:
Write a function called `find_indices` that takes two parameters: a list of integers `nums` and a list of target integers `targets`. The function should return a string containing the index of the first occurrence of each target in `nums`. If a target is not found, the string should indicate that it was not found. The string should be formatted as "Target X is at index Y, Target Z is not found, ...". Note that the function should not include any trailing commas or spaces in the output string.
"""

def find_indices(nums, targets):
    result = ""
    for target in targets:
        if target in nums:
            idx = nums.index(target)
            result += "Target {} is at index {}, ".format(target, idx)
        else:
            result += "Target {} is not found, ".format(target)
    return result[:-2]  # to remove the extra comma and space at the end
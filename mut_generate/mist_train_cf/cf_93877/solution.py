"""
QUESTION:
Write a function `remove_element(nums, val)` that removes all occurrences of `val` from the list `nums` and returns the modified list. The function should have a time complexity of O(n), where n is the length of `nums`, and a space complexity of O(1). The function cannot use built-in Python functions or methods for removing elements from a list.
"""

def remove_element(nums, val):
    i, j = 0, 0
    n = len(nums)
    while j < n:
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
        j += 1
    nums = nums[:i]
    return nums
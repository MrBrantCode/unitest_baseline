"""
QUESTION:
Write a function called `search` that takes a rotated, non-decreasing integer array `nums` with possible duplicates and an integer `target` as input. The function should return the index of `target` if it exists in `nums`, or `-1` if it does not. If `target` appears more than once, return the index of its initial occurrence. The array `nums` is guaranteed to be rotated at a certain pivot, and its length is between 1 and 5000 inclusive. The values in `nums` and the `target` are between -10^4 and 10^4 inclusive.
"""

def search(nums, target):
    if not nums:
        return -1
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1
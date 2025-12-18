"""
QUESTION:
Find the maximum length of a non-decreasing subarray in a list of at least 5 integers, where the elements are either strictly increasing or the same. The function `find_max_length(arr)` should take a list `arr` as input and return the maximum length of such a subarray.
"""

def entance(nums):
    max_length = 0
    current_length = 1

    for i in range(1, len(nums)):
        if nums[i] >= nums[i-1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1

    max_length = max(max_length, current_length)
    return max_length
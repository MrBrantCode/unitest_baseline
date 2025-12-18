"""
QUESTION:
Write a function named `check_increasing_subsequence` that takes a list of integers as input and returns `True` if there exists an increasing subsequence of length 5 in the list and `False` otherwise. The function should not modify the input list and should have a time complexity of O(n), where n is the number of elements in the input list. The input list is guaranteed to have at least 5 elements.
"""

def check_increasing_subsequence(nums):
    n = len(nums)
    if n < 5:
        return False

    for i in range(n - 4):
        if nums[i] < nums[i+1] < nums[i+2] < nums[i+3] < nums[i+4]:
            return True

    return False
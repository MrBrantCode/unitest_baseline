"""
QUESTION:
Write a function `find_missing_number(nums)` that takes a list of integers `nums` as input, where the list contains all integers from 1 to `n` except for one missing number. The function should return the missing number. The input list is guaranteed to have `n-1` elements. The solution must have a time complexity of O(n) and a space complexity of O(1).
"""

def find_missing_number(nums):
    n = len(nums) + 1
    total_sum = (n * (n + 1)) // 2
    list_sum = sum(nums)
    return total_sum - list_sum
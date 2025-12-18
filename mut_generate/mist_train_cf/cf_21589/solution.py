"""
QUESTION:
Write a function named `find_missing_number` that takes a list of integers `nums` as input, where the list contains distinct integers from 1 to n but one integer is missing. The function should return the missing integer. The function must have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the input list.
"""

def find_missing_number(nums):
    n = len(nums) + 1
    total_sum = (n * (n + 1)) // 2
    list_sum = sum(nums)
    return total_sum - list_sum
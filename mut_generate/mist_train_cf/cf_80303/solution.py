"""
QUESTION:
Write a function `findSingle(nums)` that takes a list of integers as input, where each integer occurs exactly twice except for one. The function should return the integer that occurs only once. Assume the list contains at least one such integer.
"""

def findSingle(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
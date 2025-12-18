"""
QUESTION:
Design a function `find_missing(nums)` that takes a list of integers `nums` as input and returns the smallest positive integer missing from the list. Assume the list contains distinct integers. If all positive integers from 1 to n (where n is the length of the list) are present in the list, the function should return None.
"""

def find_missing(nums):
    count = 1
    for num in nums:
        if not count in nums:
            return count
        count += 1
    return None
"""
QUESTION:
Write a function `get_min_max` that takes a list of numbers as input and returns a tuple containing the minimum and maximum values from the list. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def get_min_max(nums):
    min_val, max_val = float('inf'), float('-inf')
    for num in nums:
        min_val = min(min_val, num)
        max_val = max(max_val, num)
    return min_val, max_val
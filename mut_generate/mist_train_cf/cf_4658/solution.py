"""
QUESTION:
Write a function named `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate elements removed while maintaining the original order. The function should have a time complexity of O(n) and should not use any built-in functions or libraries for removing duplicates, any additional data structures (e.g., sets), or modify the original list in-place.
"""

def remove_duplicates(nums):
    seen = {}
    result = []
    for item in nums:
        if item not in seen:
            seen[item] = True
            result.append(item)
    return result
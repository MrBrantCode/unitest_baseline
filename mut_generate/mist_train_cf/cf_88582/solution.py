"""
QUESTION:
Write a function `remove_duplicates` that takes a list of integers as input and returns a new list containing the same elements in the same order, but with all duplicates removed. The function should have a time complexity of O(n), should not use any built-in functions or libraries for removing duplicates, and should not use any additional data structures other than a dictionary or modify the original list in-place.
"""

def remove_duplicates(nums):
    seen = {}
    result = []

    for item in nums:
        if item not in seen:
            seen[item] = True
            result.append(item)

    return result
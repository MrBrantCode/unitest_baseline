"""
QUESTION:
Write a function `find_duplicates(nums)` that takes a list of integers as input and returns a list of tuples, where each tuple contains a duplicate value and its first index in the list. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def find_duplicates(nums):
    seen = {}
    duplicates = []

    for i, num in enumerate(nums):
        if num in seen:
            duplicates.append((num, seen[num]))
        seen[num] = i

    return duplicates
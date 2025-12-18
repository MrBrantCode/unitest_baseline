"""
QUESTION:
Write a function `find_duplicates(nums)` that takes a list of integers `nums` as input and returns a list of tuples, where each tuple contains a duplicate value from the list and its first occurrence index. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def find_duplicates(nums):
    seen = {}
    duplicates = []

    for i, num in enumerate(nums):
        if num in seen:
            duplicates.append((num, seen[num]))
        seen[num] = i

    return duplicates
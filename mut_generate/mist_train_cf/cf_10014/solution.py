"""
QUESTION:
Write a function called `remove_duplicates` that takes a list of integers as input, removes duplicates while preserving the original order of elements, and returns the new list. The function should have a time complexity of O(n) and a space complexity of O(n).
"""

def remove_duplicates(nums):
    unique_nums = []
    seen = set()
    for num in nums:
        if num not in seen:
            unique_nums.append(num)
            seen.add(num)
    return unique_nums
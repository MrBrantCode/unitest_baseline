"""
QUESTION:
Create a function called `remove_duplicates` that takes a list of integers as input. The function should return a new list with only the unique elements from the input list, in the same order as they appeared in the original list. The function should be able to handle lists with negative integers, empty lists, non-consecutive duplicates, and large lists with millions of elements, all within a time complexity of O(n) or less.
"""

def remove_duplicates(nums):
    unique_nums = []
    seen_nums = set()

    for num in nums:
        if num not in seen_nums:
            unique_nums.append(num)
            seen_nums.add(num)

    return unique_nums
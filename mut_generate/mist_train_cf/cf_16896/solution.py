"""
QUESTION:
Create a function `sort_nums` that takes a list of mixed data types as input. The function should filter out numbers less than 5, non-numeric values, and duplicates, then sort the remaining numbers in descending order. The output should be a list of unique numbers.
"""

def sort_nums(nums):
    unique_nums = [num for num in set(nums) if isinstance(num, int) and num >= 5]
    unique_nums.sort(reverse=True)
    return unique_nums
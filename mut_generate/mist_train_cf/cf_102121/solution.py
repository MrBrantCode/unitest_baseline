"""
QUESTION:
Create a function called `get_sorted_unique_even_numbers` that takes a list of integers as input, filters out the even numbers, removes duplicates, and returns the resulting list in descending order. The function should not modify the original input list.
"""

def get_sorted_unique_even_numbers(nums):
    even_nums = [num for num in set(nums) if num % 2 == 0]
    even_nums.sort(reverse=True)
    return even_nums
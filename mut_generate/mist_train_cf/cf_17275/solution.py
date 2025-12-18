"""
QUESTION:
Create a function `even_nums_sorted` that takes a list of integers as input, filters out the even numbers, and returns them in a new list sorted in descending order.
"""

def even_nums_sorted(nums):
    even_nums = [num for num in nums if num % 2 == 0]
    even_nums.sort(reverse=True)
    return even_nums
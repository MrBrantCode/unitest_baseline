"""
QUESTION:
Create a function `sort_even_nums` that takes a list of integers as input and returns a new list containing only the even numbers from the input list, sorted in descending order.
"""

def sort_even_nums(nums):
    even_nums = [num for num in nums if num % 2 == 0]
    even_nums.sort(reverse=True)
    return even_nums
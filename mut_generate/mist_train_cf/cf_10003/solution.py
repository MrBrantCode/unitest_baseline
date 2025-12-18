"""
QUESTION:
Write a function, square_even_numbers, that takes a list of integers as input, squares the even numbers, and returns them in a new list. The function should only include the squared even numbers in the output list, and ignore the odd numbers.
"""

def square_even_numbers(nums):
    return [num ** 2 for num in nums if num % 2 == 0]
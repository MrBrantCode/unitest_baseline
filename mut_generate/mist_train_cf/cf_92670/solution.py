"""
QUESTION:
Create a function `filter_odd_numbers` that takes a list of integers as input, filters out the even numbers, and returns the remaining odd numbers in a new list sorted in descending order.
"""

def filter_odd_numbers(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    odd_numbers.sort(reverse=True)
    return odd_numbers
"""
QUESTION:
Write a function called `filter_odd_numbers` that takes a list of integers as input, returns a new list containing only the odd numbers from the original list, and sorts them in descending order.
"""

def filter_odd_numbers(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    odd_numbers.sort(reverse=True)
    return odd_numbers
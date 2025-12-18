"""
QUESTION:
Create a function called `filter_numbers` that takes a list of integers as input. The function should return a new list containing only the numbers that are greater than 5 and divisible by 2.
"""

def filter_numbers(numbers):
    return [num for num in numbers if num > 5 and num % 2 == 0]
"""
QUESTION:
Write a function named `sum_of_odd_numbers` that accepts a list of integers and returns the cumulative sum of all the odd numbers in the list.
"""

def sum_of_odd_numbers(numbers):
    return sum(num for num in numbers if num % 2 != 0)
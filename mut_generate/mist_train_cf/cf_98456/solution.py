"""
QUESTION:
Write a Python function named `sum_of_even_numbers` that takes a list of numbers as input, calculates the sum of all even numbers in the list, and returns the total sum.
"""

def sum_of_even_numbers(numbers):
    even_numbers = [number for number in numbers if number % 2 == 0]
    return sum(even_numbers)
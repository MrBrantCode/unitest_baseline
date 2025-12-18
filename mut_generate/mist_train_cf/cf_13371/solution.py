"""
QUESTION:
Create a function called `sum_even_numbers` that calculates the sum of even numbers in a given list of integers. The function should only consider numbers that are divisible by 2 as even numbers and exclude all other numbers from the sum.
"""

def sum_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)
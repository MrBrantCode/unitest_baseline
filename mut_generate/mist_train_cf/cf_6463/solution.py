"""
QUESTION:
Write a function `calculate_even_sum` that takes a list of integers as input, removes any duplicate numbers, and returns the sum of the remaining even numbers that are between 10 and 100 (inclusive).
"""

def calculate_even_sum(numbers):
    unique_numbers = list(set(numbers))
    even_sum = sum(num for num in unique_numbers if 10 <= num <= 100 and num % 2 == 0)
    return even_sum
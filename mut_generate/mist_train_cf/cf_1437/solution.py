"""
QUESTION:
Create a function named `filter_and_sort` that takes a list of integers as input, filters out the numbers that are divisible by both 3 and 4, and returns the remaining numbers in descending order.
"""

def filter_and_sort(numbers):
    filtered_numbers = [num for num in numbers if num % 3 != 0 or num % 4 != 0]
    filtered_numbers.sort(reverse=True)
    return filtered_numbers
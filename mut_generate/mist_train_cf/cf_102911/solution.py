"""
QUESTION:
Implement a function named `get_unique_even_numbers` that takes a list of integers as input and returns a set containing the unique even numbers from the list.
"""

def get_unique_even_numbers(numbers):
    unique_even_numbers = set()
    for num in numbers:
        if num % 2 == 0:
            unique_even_numbers.add(num)
    return unique_even_numbers
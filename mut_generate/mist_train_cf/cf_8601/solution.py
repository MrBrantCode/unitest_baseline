"""
QUESTION:
Create a function named `sort_even_odd` that takes a list of integers as input. The function should return the sorted list of even numbers in ascending order if the list contains only even numbers. If the list contains any odd numbers, remove them from the list and return the sorted list of remaining even numbers.
"""

def sort_even_odd(numbers):
    even_numbers = [number for number in numbers if number % 2 == 0]
    
    if any(number % 2 != 0 for number in numbers):
        return sorted(even_numbers)

    return sorted(even_numbers)
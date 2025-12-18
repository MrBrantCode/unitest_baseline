"""
QUESTION:
Create a function called `get_even_sorted` that takes a list of integers as input, filters out the even numbers, and returns them in a new list sorted in ascending order. The function should not modify the original list.
"""

def get_even_sorted(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    even_numbers.sort()
    return even_numbers
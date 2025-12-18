"""
QUESTION:
Write a function `sort_even_odd(numbers)` that takes a list of integers as input. If the list contains only even numbers, sort them in ascending order. If the list contains any odd numbers, sort the even numbers in ascending order, remove the odd numbers, and return the sorted list of even numbers.
"""

def sort_even_odd(numbers):
    if all(num % 2 == 0 for num in numbers):
        return sorted([num for num in numbers if num % 2 == 0])
    else:
        return sorted([num for num in numbers if num % 2 == 0])
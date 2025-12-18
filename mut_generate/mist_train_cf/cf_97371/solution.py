"""
QUESTION:
Write a function named `sort_even_odd` that takes a list of integers as input. The function should check if the list contains only even numbers, sort the even numbers in ascending order, and then sort the odd numbers in descending order. The function should return a single list containing the sorted even numbers followed by the sorted odd numbers.
"""

def sort_even_odd(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]

    even_numbers.sort()
    odd_numbers.sort(reverse=True)

    return even_numbers + odd_numbers
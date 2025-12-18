"""
QUESTION:
Write a function named sum_even_numbers that takes a list of integers as input and returns the sum of all the even numbers in the list. The function should have a time complexity of O(n) and space complexity of O(1).
"""

def sum_even_numbers(numbers):
    """Returns the sum of all the even numbers in the input list."""
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
    return even_sum
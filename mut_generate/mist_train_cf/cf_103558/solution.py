"""
QUESTION:
Create a function `sort_numbers(numbers)` that takes a list of integers as input and returns the sorted list where all odd numbers are placed first in their original order, followed by the even numbers in descending order.
"""

def sort_numbers(numbers):
    """
    Sorts a list of integers where all odd numbers are placed first in their original order, 
    followed by the even numbers in descending order.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: The sorted list of integers.
    """
    odds = []
    evens = []

    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)

    evens.sort(reverse=True)

    return odds + evens
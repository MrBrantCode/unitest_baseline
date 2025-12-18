"""
QUESTION:
Write a function named `sum_positive_numbers` that takes a list of integers as input. The function should return the sum of all positive integers in the list, after removing duplicates and sorting the list in descending order. If the list is empty or contains no positive integers, the function should return 0.
"""

def entrance(numbers):
    if not numbers:
        return 0
    numbers = list(set([num for num in numbers if num > 0]))
    numbers.sort(reverse=True)
    return sum(numbers)
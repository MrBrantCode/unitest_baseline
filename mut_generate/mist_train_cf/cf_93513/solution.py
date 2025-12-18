"""
QUESTION:
Write a function named `sum_positive_numbers` that takes a list of numbers as input and returns the sum of all positive numbers in the list using recursion. The function should exclude negative numbers from the sum. If the list is empty, it should return 0.
"""

def sum_positive_numbers(numbers):
    if len(numbers) == 0:
        return 0
    elif numbers[0] < 0:
        return sum_positive_numbers(numbers[1:])
    else:
        return numbers[0] + sum_positive_numbers(numbers[1:])
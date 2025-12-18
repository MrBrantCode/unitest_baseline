"""
QUESTION:
Write a function named `sum_excluding_multiples` that takes an array of integers as input and returns the sum of all numbers in the array, excluding those that are divisible by 3 or 5.
"""

def sum_excluding_multiples(numbers):
    total = 0
    for number in numbers:
        if number % 3 != 0 and number % 5 != 0:
            total += number
    return total
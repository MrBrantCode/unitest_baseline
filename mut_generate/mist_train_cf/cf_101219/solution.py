"""
QUESTION:
Write a function named `sum_of_even_numbers` that calculates the sum of all even integers in a given list. The function should handle edge cases such as empty lists, non-integer values, and negative numbers, and must run in linear time and space complexity.
"""

def sum_of_even_numbers(numbers):
    total = 0
    for number in numbers:
        if isinstance(number, int) and number % 2 == 0:
            total += number
    return total
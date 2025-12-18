"""
QUESTION:
Write a function `sum_even_numbers` that calculates the sum of all even numbers in a given list without using loops or built-in functions for sum calculation or even number check. The function should have a time complexity of O(n) and a space complexity of O(1), handling empty lists by returning 0.
"""

def sum_even_numbers(numbers):
    if len(numbers) == 0:
        return 0
    elif numbers[0] % 2 == 0:
        return numbers[0] + sum_even_numbers(numbers[1:])
    else:
        return sum_even_numbers(numbers[1:])
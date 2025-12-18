"""
QUESTION:
Create a function called `sum_positive_even_numbers` that takes a list of numbers as input and returns the sum of all unique positive even numbers in the list, ignoring duplicates. The function should have a time complexity of O(n), where n is the length of the list, and should not use the built-in sum() function or any external libraries.
"""

def sum_positive_even_numbers(numbers):
    unique_numbers = set()
    total = 0

    for number in numbers:
        if number > 0 and number % 2 == 0 and number not in unique_numbers:
            total += number
            unique_numbers.add(number)

    return total
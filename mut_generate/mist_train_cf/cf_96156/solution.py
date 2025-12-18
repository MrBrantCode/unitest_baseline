"""
QUESTION:
Create a function called `calculate_sum` that takes a list of positive numbers as input and returns the sum of all numbers in the list. The function should not use any built-in functions like `sum()` or `reduce()` and should be able to handle lists of up to 10^6 numbers efficiently.
"""

def calculate_sum(numbers):
    total_sum = 0
    for number in numbers:
        total_sum += number
    return total_sum
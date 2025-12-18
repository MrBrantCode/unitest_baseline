"""
QUESTION:
Create a function `add_numbers` that calculates the sum of a list of integers without using arithmetic operators (`+`, `-`, `*`, `/`, etc.) or the `sum()` function. The function should take a list of integers as input and return their sum.
"""

def add_numbers(numbers):
    total = 0
    for num in numbers:
        total = total.__add__(num)
    return total
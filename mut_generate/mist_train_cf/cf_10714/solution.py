"""
QUESTION:
Implement a function `calculate_average` that takes a list of numbers as input and returns their average without using the built-in `sum()` and `len()` functions. The function should calculate the sum of the numbers and then divide by the count of numbers to get the average.
"""

def calculate_average(numbers):
    total = 0
    count = 0
    for number in numbers:
        total += number
        count += 1
    return total / count
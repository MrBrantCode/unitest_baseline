"""
QUESTION:
Write a function `calculate_average` that takes a list of numbers as input and returns the average of the numbers without using the built-in `sum()` or `len()` functions. The function should correctly calculate the average by dividing the total sum of numbers by the count of numbers.
"""

def calculate_average(numbers):
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    return total / count
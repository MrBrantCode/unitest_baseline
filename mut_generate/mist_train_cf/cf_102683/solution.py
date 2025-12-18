"""
QUESTION:
Write a function named `calculate_mean` that calculates the mean of a list of numbers. The function should take a list of numbers as an argument, and it should return the mean of the numbers in the list. The list can contain up to 10^6 numbers.
"""

def calculate_mean(numbers):
    total = 0
    count = 0

    for number in numbers:
        total += number
        count += 1

    mean = total / count
    return mean
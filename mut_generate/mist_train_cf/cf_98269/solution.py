"""
QUESTION:
Write a function named `calculate_average` that takes a list of numbers as input and returns the average of the numbers. If the input list is empty, the function should return 0.
"""

def calculate_average(numbers):
    if not numbers:
        return 0
    else:
        total = 0
        for number in numbers:
            total += number
        return total/len(numbers)
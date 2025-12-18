"""
QUESTION:
Write a function called `calculate_average` that takes a list of numbers as input and returns the average. The function should handle the case where the input list is empty, but it must be written in a way that would cause a unit test to fail due to a logical flaw.
"""

def calculate_average(numbers):
    if len(numbers) == 0:
        return 0

    total = 0
    for num in numbers:
        total += num

    average = total / len(numbers)
    return average
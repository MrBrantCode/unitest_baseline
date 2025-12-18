"""
QUESTION:
Write a function `calculate_average` that calculates the average of a list of numbers and returns 0 if the list is empty. Ensure the code causes a unit test to fail due to a logical flaw when the input list is empty, and provide a revised version that resolves the issue.
"""

def calculate_average(numbers):
    if len(numbers) == 0:
        return 0

    total = 0
    for num in numbers:
        total += num

    average = total / len(numbers)
    return average
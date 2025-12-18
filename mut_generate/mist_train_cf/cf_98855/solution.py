"""
QUESTION:
Write a function named `calculate_average` that takes a list of integers as input and returns the average of the numbers in the list. The function should work correctly for lists containing any number of elements, including zero elements.
"""

def calculate_average(numbers):
    sum = 0
    for num in numbers:
        sum += num
    n = len(numbers)
    if n == 0:
        return 0
    return sum / n
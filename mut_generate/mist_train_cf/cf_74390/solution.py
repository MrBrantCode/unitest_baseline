"""
QUESTION:
Create a function named `penultimate_highest` that takes a list of integers as input and returns the second highest unique numerical value. If the list has less than two unique values, the function should return an appropriate value or message.
"""

def penultimate_highest(numbers):
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        return "List should have at least two unique values."
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]
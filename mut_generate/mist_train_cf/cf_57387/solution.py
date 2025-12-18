"""
QUESTION:
Write a function named `penultimate_smallest` that takes a sequence of decimal values as input and returns the penultimate smallest magnitude from the set of values. The function should handle sequences with less than two unique values and return a meaningful message in such cases. Assume the input sequence contains at least one value.
"""

def penultimate_smallest(numbers):
    numbers = list(set(numbers))  # remove duplicates
    numbers.sort()
    return numbers[1] if len(numbers) >= 2 else "Not Available"
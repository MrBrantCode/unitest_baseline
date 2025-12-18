"""
QUESTION:
Write a function `third_max` that takes a list of unique random numbers as input and returns the third highest maximum value. The input list may have less than three unique numbers.
"""

def third_max(numbers):
    if len(numbers) < 3:
        return "Not enough numbers in sequence"
    numbers.sort(reverse=True)
    return numbers[2]
"""
QUESTION:
Write a function called `get_mean` that calculates the mean of a given list of up to 1 million numbers and returns the result rounded to 2 decimal places. The input list will only contain numbers.
"""

def get_mean(numbers):
    return round(sum(numbers) / len(numbers), 2)
"""
QUESTION:
Write a function named `correct_mean` that calculates the mean of a given list of integers. The function should be efficient enough to handle lists with a length of over 10,000 elements within a reasonable time frame and should return a floating-point number to preserve the precision of the mean.
"""

def correct_mean(numbers):
    total = sum(numbers)
    mean = total / len(numbers)
    return mean
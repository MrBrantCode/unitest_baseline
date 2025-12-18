"""
QUESTION:
Create a function `find_mean` that calculates the mean (average) of a list of numbers. The function should be able to handle lists of up to 10^6 numbers and have a time complexity of O(n). The function should take a list of numbers as input and return the calculated mean.
"""

def find_mean(numbers):
    total = 0
    for num in numbers:
        total += num
    mean = total / len(numbers)
    return mean
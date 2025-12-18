"""
QUESTION:
Create a function `calculate_stats(data)` that calculates the mean, variance, and standard deviation of a given list of numbers. The function should take a list of numbers as input and return a tuple containing the mean, variance, and standard deviation. It should also handle edge cases such as empty lists and lists with only a single number.
"""

def calculate_stats(data):
    n = len(data)
    if n == 0:
        return (0, 0, 0)
    elif n == 1:
        return (data[0], 0, 0)
    else:
        mean = sum(data) / n
        variance = sum((num - mean) ** 2 for num in data) / n
        std = variance ** 0.5
        return (mean, variance, std)
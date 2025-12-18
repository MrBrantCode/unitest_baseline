"""
QUESTION:
Create a function 'find_average' that calculates and returns the mean and standard deviation of a list of numbers. The function should take a list of numbers as input and return a tuple containing the mean and the standard deviation. The standard deviation should be calculated with a degree of freedom of N-1, where N is the number of numbers in the list.
"""

def find_average(numbers):
    total = sum(numbers)
    mean = total / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1)
    standard_deviation = variance ** 0.5
    return mean, standard_deviation
"""
QUESTION:
Write a function named `standard_deviation` that calculates the standard deviation of a list of numbers. The function should not use any statistical libraries. It should take a list of numbers as input and return the standard deviation of the input list. The function should calculate the mean of the input list, then calculate the variance by summing the squared deviations from the mean and dividing by the number of observations. Finally, it should return the square root of the variance.
"""

def standard_deviation(lst):
    # Number of observations
    n = len(lst)

    # Mean of the data
    mean = sum(lst) / n

    # Square deviations
    deviations = [(x - mean) ** 2 for x in lst]

    # Variance
    variance = sum(deviations) / n

    # Standard Deviation
    std_dev = variance**0.5

    return std_dev
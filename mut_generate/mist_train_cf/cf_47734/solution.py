"""
QUESTION:
Write a function called `calculate_std_dev` that calculates the standard deviation of a list of numbers. The function should take a list of numbers as input and return the standard deviation of the list. The standard deviation should be calculated manually without using any external libraries.
"""

def calculate_std_dev(num_list):
    # Calculate the mean
    mean = sum(num_list) / len(num_list)
    # Calculate variance
    variance = sum([((x - mean) ** 2) for x in num_list]) / len(num_list)
    # Calculate standard deviation
    std_dev = variance ** 0.5
    return std_dev
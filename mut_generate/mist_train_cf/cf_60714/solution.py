"""
QUESTION:
Write a standalone Python function `calculate_mean_stddev(data)` that calculates both the mean and standard deviation of a given list of numbers. The function should handle edge cases such as empty lists, and should not use any in-built or external libraries. The input list may contain both integers and floating point numbers.
"""

def calculate_mean_stddev(data):
    # Handling edge case
    if len(data) == 0:
        return None, None

    # Calculate mean
    sum_of_data = sum(data)
    mean = sum_of_data / len(data)

    # Calculate standard deviation
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    stddev = variance ** 0.5

    return mean, stddev
"""
QUESTION:
Write a function `calculate_std_dev` that takes an array of integers as input and returns the standard deviation of the array with a precision of at least 4 decimal places. The function should only consider values less than or equal to 100 and must not use any built-in functions or libraries for calculating the standard deviation. The input array is guaranteed to have a length of at least 100 elements.
"""

def calculate_std_dev(array):
    # Exclude values greater than 100
    filtered_array = [x for x in array if x <= 100]

    # Calculate mean
    mean = sum(filtered_array) / len(filtered_array)

    # Calculate squared differences from the mean
    squared_diffs = [(x - mean) ** 2 for x in filtered_array]

    # Calculate variance
    variance = sum(squared_diffs) / len(squared_diffs)

    # Calculate standard deviation
    std_dev = variance ** 0.5

    return round(std_dev, 4)
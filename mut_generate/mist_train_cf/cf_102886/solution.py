"""
QUESTION:
Create a function named `calculate_statistics` that calculates the mean, median, mode, and standard deviation of a given set of data. The function should be able to handle datasets with missing values by excluding them from calculations. The input dataset is a list of numbers that may contain `None` values, which represent missing values.
"""

import statistics

def calculate_statistics(data):
    """
    Calculate the mean, median, mode, and standard deviation of a given set of data.
    
    Parameters:
    data (list): A list of numbers that may contain None values, which represent missing values.
    
    Returns:
    dict: A dictionary containing the mean, median, mode, and standard deviation of the input data.
    """
    
    # Remove missing values
    cleaned_data = [x for x in data if x is not None]
    
    # Calculate mean
    mean = statistics.mean(cleaned_data)
    
    # Calculate median
    median = statistics.median(cleaned_data)
    
    # Calculate mode
    mode = statistics.mode(cleaned_data)
    
    # Calculate standard deviation
    std_dev = statistics.stdev(cleaned_data)
    
    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "std_dev": std_dev
    }
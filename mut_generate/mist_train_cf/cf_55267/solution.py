"""
QUESTION:
Create a function `calculate_mean` that takes a list of values as input, removes any non-integer values, sorts the remaining integers in ascending order, and calculates the arithmetic mean of the sorted integers. The function should return the mean value and the sorted list of integers. If the list becomes empty after removing non-integer values, the function should return `None` as the mean value. The function should be efficient enough to handle large datasets.
"""

def calculate_mean(values):
    # Filter out non-integer values
    values = [i for i in values if isinstance(i, int)]
    
    # Sort the list in ascending order
    values.sort()
    
    # Calculate the mean value
    mean_value = sum(values) / len(values) if values else None
    
    return mean_value, values
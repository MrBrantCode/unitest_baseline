"""
QUESTION:
Implement a function named `calculate_std_dev` that calculates the standard deviation of a list of numbers without using any libraries, instead using the statistical formula. The function should handle large data sets efficiently and have a time complexity proportional to the size of the dataset.
"""

def calculate_std_dev(numbers):
    """
    Calculate the standard deviation of a list of numbers without using any libraries.
    
    Args:
        numbers (list): A list of numbers.
    
    Returns:
        float: The standard deviation of the input numbers.
    """
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance ** 0.5
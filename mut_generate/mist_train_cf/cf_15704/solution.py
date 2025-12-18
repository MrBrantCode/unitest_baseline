"""
QUESTION:
Create a function `calculate_sum` that takes an array of integers as input and returns the sum of all values less than 10. If a value is 10 or greater, skip it and print a warning message. The array may contain negative numbers.
"""

def calculate_sum(array):
    """
    This function calculates the sum of all values less than 10 in a given array.
    
    Parameters:
    array (list): A list of integers.
    
    Returns:
    int: The sum of all values less than 10 in the array.
    """
    total_sum = 0
    for value in array:
        if value >= 10:
            print("Warning: Skipping value", value)
        else:
            total_sum += value
    return total_sum
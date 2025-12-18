"""
QUESTION:
Create a function named 'calculate_statistics' that takes a list of numbers as input and returns the sum, average, maximum, and minimum values of the list. The numbers in the list can be positive, negative, or zero, and can be integers or floating-point numbers. The function should return the results accurate to two decimal places.
"""

def calculate_statistics(numbers):
    """
    Calculate the sum, average, maximum, and minimum values of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        dict: A dictionary containing the sum, average, maximum, and minimum values.
    """

    # Calculate the sum of all the numbers
    sum_of_numbers = sum(numbers)
    
    # Calculate the average of the numbers
    average = sum_of_numbers / len(numbers)
    
    # Find the maximum value in the list
    maximum_value = max(numbers)
    
    # Find the minimum value in the list
    minimum_value = min(numbers)
    
    # Return the results accurate to two decimal places
    return {
        "sum": round(sum_of_numbers, 2),
        "average": round(average, 2),
        "maximum": round(maximum_value, 2),
        "minimum": round(minimum_value, 2)
    }
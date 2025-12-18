"""
QUESTION:
Write a function named 'calculate_statistics' that takes a list of numbers as input and returns the maximum, minimum, average, sum, and product of the numbers in the list. The function should handle any list of numbers, not just the provided example.
"""

def calculate_statistics(number_list):
    """
    This function calculates the maximum, minimum, average, sum, and product of a given list of numbers.
    
    Args:
        number_list (list): A list of numbers.
    
    Returns:
        dict: A dictionary containing the maximum, minimum, average, sum, and product of the numbers in the list.
    """

    maximum = max(number_list)
    minimum = min(number_list)
    average = sum(number_list) / len(number_list)
    total_sum = sum(number_list)
    product = 1

    for num in number_list:
        product *= num

    return {
        "Maximum": maximum,
        "Minimum": minimum,
        "Average": average,
        "Sum": total_sum,
        "Product": product
    }
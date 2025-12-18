"""
QUESTION:
Write a function named `calculate_odd_product` that takes a string as input, extracts all numerical values from the string, filters out the odd numbers, and returns their product. The function should handle strings containing non-numeric characters.
"""

def calculate_odd_product(s):
    """
    This function calculates the product of all odd numbers found in a given string.
    
    Parameters:
    s (str): The input string containing numerical values.
    
    Returns:
    int: The product of all odd numbers in the string.
    """
    # Extract all numerical values from the string and convert them to integers
    numbers = [int(num) for num in s.split() if num.isdigit()]
    
    # Filter out the odd numbers
    odd_numbers = [num for num in numbers if num % 2 != 0]
    
    # Calculate the product of the odd numbers
    product = 1
    for num in odd_numbers:
        product *= num
    
    return product
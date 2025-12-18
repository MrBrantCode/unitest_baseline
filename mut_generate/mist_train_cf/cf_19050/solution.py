"""
QUESTION:
Write a function named `sum_of_digits` that takes a string as input and returns the sum of all the digits in the string, excluding any non-digit characters. The function should iterate over each character in the string and add up the digits found.
"""

def sum_of_digits(s):
    """
    This function calculates the sum of all the digits in a given string.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The sum of all the digits in the string.
    """
    return sum(int(char) for char in s if char.isdigit())
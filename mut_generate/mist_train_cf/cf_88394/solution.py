"""
QUESTION:
Write a function named `sum_of_digits` that takes a string as input and returns the sum of all the digits in the string, excluding any non-digit characters. The function should be able to handle strings containing punctuation marks, special characters, and letters, in addition to digits.
"""

def sum_of_digits(input_string):
    """
    This function calculates the sum of all the digits in a given string, 
    excluding any non-digit characters.
    
    Args:
        input_string (str): The input string containing digits and/or non-digit characters.
    
    Returns:
        int: The sum of all the digits in the input string.
    """
    return sum(int(char) for char in input_string if char.isdigit())
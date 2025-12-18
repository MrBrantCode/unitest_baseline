"""
QUESTION:
Write a function named `convert_and_check` that takes a string of numbers as input, where the string contains only positive integers with a maximum length of 10 characters. The function should return two values: an integer converted from the input string (ignoring leading zeros) and a boolean indicating whether the input string is a palindrome.
"""

def convert_and_check(input_str):
    """
    Converts a string of numbers to an integer (ignoring leading zeros) and checks if the string is a palindrome.

    Args:
        input_str (str): A string of numbers with a maximum length of 10 characters.

    Returns:
        tuple: A tuple containing the converted integer and a boolean indicating whether the input string is a palindrome.
    """

    # Remove leading zeros
    input_str = input_str.lstrip('0')
    
    # Convert string to integer
    integer_val = int(input_str)
    
    # Check if string is equal to its reverse
    is_palindrome = input_str == input_str[::-1]
    
    return integer_val, is_palindrome
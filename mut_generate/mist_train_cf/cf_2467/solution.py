"""
QUESTION:
Write a function called `sum_even_ascii` that takes a string as input, calculates the sum of the ASCII values of only the even alphabetic characters in the string, and returns this sum. The input string will have at most 100 characters. Non-alphabetic characters should be ignored.
"""

def sum_even_ascii(string):
    """
    Calculate the sum of ASCII values of only the even alphabetic characters in the string.

    Args:
    string (str): The input string.

    Returns:
    int: The sum of even ASCII values of alphabetic characters.
    """
    ascii_sum = 0
    for char in string:
        if char.isalpha():
            ascii_value = ord(char)
            if ascii_value % 2 == 0:
                ascii_sum += ascii_value
    return ascii_sum
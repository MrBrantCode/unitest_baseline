"""
QUESTION:
Write a function `reverse_string` that takes a string `input_string` as input and returns a new string that is the reverse of the `input_string`. Do not use any built-in functions or methods that directly reverse a string; instead, implement the reversal logic yourself.
"""

def reverse_string(input_string):
    """
    Returns a new string that is the reverse of the input_string.

    :param input_string: The string to be reversed
    :return: A new string that is the reverse of the input_string
    """
    reversed_string = ""
    for i in range(len(input_string) - 1, -1, -1):
        reversed_string += input_string[i]
    return reversed_string
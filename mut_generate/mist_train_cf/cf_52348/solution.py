"""
QUESTION:
Create a function `reverse_and_greet` that takes an input string, reverses it, and returns a new string that starts with "Hola, " followed by the reversed input string.
"""

def reverse_and_greet(input_string: str) -> str:
    """
    Reverses the input string and returns a new string that starts with 'Hola, ' 
    followed by the reversed input string.

    Args:
        input_string (str): The input string to be reversed.

    Returns:
        str: A new string that starts with 'Hola, ' followed by the reversed input string.
    """
    reversed_string = input_string[::-1]
    return "Hola, " + reversed_string
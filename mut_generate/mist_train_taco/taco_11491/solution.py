"""
QUESTION:
Move every letter in the provided string forward 10 letters through the alphabet.

If it goes past 'z', start again at 'a'.

Input will be a string with length > 0.
"""

from string import ascii_lowercase as al

def move_letters_forward(input_string: str, steps: int = 10) -> str:
    """
    Move every letter in the provided string forward by the specified number of steps through the alphabet.
    If it goes past 'z', start again at 'a'.

    :param input_string: The input string whose letters need to be moved forward.
    :param steps: The number of steps to move each letter forward. Default is 10.
    :return: The resulting string after moving each letter forward by the specified number of steps.
    """
    # Create a translation table for the specified number of steps
    tbl = str.maketrans(al, al[steps:] + al[:steps])
    
    # Translate the input string using the translation table
    output_string = input_string.translate(tbl)
    
    return output_string
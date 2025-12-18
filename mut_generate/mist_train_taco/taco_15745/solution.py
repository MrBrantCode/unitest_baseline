"""
QUESTION:
The aim of this kata is to split a given string into different strings of equal size (note size of strings is passed to the method)

Example:

    Split the below string into other strings of size #3

    'supercalifragilisticexpialidocious'

    Will return a new string
    'sup erc ali fra gil ist ice xpi ali doc iou s'


Assumptions:

    String length is always greater than 0
    String has no spaces
    Size is always positive
"""

from textwrap import wrap

def split_string_into_parts(input_string: str, part_length: int) -> str:
    """
    Splits the input string into parts of the specified length and joins them with a space.

    Parameters:
    - input_string (str): The string to be split.
    - part_length (int): The length of each part the string should be split into.

    Returns:
    - str: The input string split into parts of the specified length, with each part separated by a space.
    """
    return ' '.join(wrap(input_string, part_length))
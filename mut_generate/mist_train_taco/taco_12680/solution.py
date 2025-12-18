"""
QUESTION:
Write a program which converts uppercase/lowercase letters to lowercase/uppercase for a given string.

Constraints

* The length of the input string < 1200

Input

A string is given in a line.

Output

Print the converted string in a line. Note that you do not need to convert any characters other than alphabetical letters.

Example

Input

fAIR, LATER, OCCASIONALLY CLOUDY.


Output

Fair, later, occasionally cloudy.
"""

def convert_case(input_string: str) -> str:
    """
    Converts uppercase letters to lowercase and lowercase letters to uppercase in the given string.

    Parameters:
    input_string (str): The input string to be converted.

    Returns:
    str: The converted string.
    """
    return input_string.swapcase()
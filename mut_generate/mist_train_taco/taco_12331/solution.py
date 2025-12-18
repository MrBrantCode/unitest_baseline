"""
QUESTION:
Write a program which replace all the lower-case letters of a given text with the corresponding captital letters.



Input

A text including lower-case letters, periods, and space is given in a line. The number of characters in the text is less than or equal to 200.

Output

Print the converted text.

Example

Input

this is a pen.


Output

THIS IS A PEN.
"""

def convert_to_uppercase(text: str) -> str:
    """
    Converts all lowercase letters in the input text to uppercase.

    Parameters:
    text (str): The input text containing lowercase letters, periods, and spaces.

    Returns:
    str: The converted text with all lowercase letters replaced by their uppercase counterparts.
    """
    return text.upper()
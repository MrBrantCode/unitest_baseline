"""
QUESTION:
Create a function called `alphabetical_order` that takes a string as input and returns the string rearranged in alphabetical order.
"""

def alphabetical_order(string):
    """
    Rearrange the given string in alphabetical order.

    Args:
        string (str): The input string.

    Returns:
        str: The input string rearranged in alphabetical order.
    """
    return ''.join(sorted(string))
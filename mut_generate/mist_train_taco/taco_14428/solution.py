"""
QUESTION:
Implement `String#whitespace?(str)` (Ruby), `String.prototype.whitespace(str)` (JavaScript), `String::whitespace(str)` (CoffeeScript), or `whitespace(str)` (Python), which should return `true/True` if given object consists exclusively of zero or more whitespace characters, `false/False` otherwise.
"""

def is_whitespace(string: str) -> bool:
    """
    Check if the given string consists exclusively of zero or more whitespace characters.

    Parameters:
    string (str): The input string to be checked.

    Returns:
    bool: True if the string consists exclusively of whitespace characters, False otherwise.
    """
    return not string or string.isspace()
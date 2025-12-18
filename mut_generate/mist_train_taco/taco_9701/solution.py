"""
QUESTION:
Implement `String#digit?` (in Java `StringUtils.isDigit(String)`), which should return `true` if given object is a digit (0-9), `false` otherwise.
"""

def is_single_digit(s: str) -> bool:
    """
    Checks if the given string is a single digit (0-9).

    Parameters:
    s (str): The input string to be checked.

    Returns:
    bool: True if the string is a single digit, False otherwise.
    """
    return s.isdigit() and len(s) == 1
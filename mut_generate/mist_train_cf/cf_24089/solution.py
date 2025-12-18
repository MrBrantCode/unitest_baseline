"""
QUESTION:
Create a regular expression pattern to match a string that only contains the characters "a", "b", and "c", with no other characters allowed. The function should match any string consisting of one or more of these three characters.
"""

def entrance(s):
    """
    This function checks if the input string only contains the characters 'a', 'b', and 'c'.

    Parameters:
    s (str): The input string to check.

    Returns:
    bool: True if the string only contains 'a', 'b', and 'c', False otherwise.
    """
    import re
    pattern = r"^[a-c]+$"
    return bool(re.match(pattern, s))
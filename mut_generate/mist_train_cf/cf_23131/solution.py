"""
QUESTION:
Create a function named `filter_strings` that takes a list of strings as input, filters out the strings that meet the following conditions, and returns the filtered list: 
1. The length of the string is greater than 10.
2. The string contains at least one uppercase letter.
3. The string contains at least one special character from the set (!@#$%^&*).
"""

def filter_strings(strings):
    """
    Filter out strings that meet the following conditions:
    1. The length of the string is greater than 10.
    2. The string contains at least one uppercase letter.
    3. The string contains at least one special character from the set (!@#$%^&*).

    Args:
        strings (list): A list of strings to be filtered.

    Returns:
        list: The filtered list of strings.
    """
    special_chars = "!@#$%^&*"
    return [string for string in strings 
            if len(string) > 10 
            and any(char.isupper() for char in string) 
            and any(char in special_chars for char in string)]
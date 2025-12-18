"""
QUESTION:
Create a function `filter_strings` that takes a list of strings as input and returns a new list containing only the strings with a length greater than 10, at least one uppercase letter, and at least one special character from the set (!@#$%^&*). The input list must contain at least 5 elements.
"""

def filter_strings(strings):
    """
    Filters a list of strings to include only strings with a length greater than 10, 
    at least one uppercase letter, and at least one special character from the set (!@#$%^&*).
    
    Args:
    strings (list): A list of strings.
    
    Returns:
    list: A new list containing the filtered strings.
    """
    special_chars = "!@#$%^&*"
    return [string for string in strings if len(string) > 10 and any(char.isupper() for char in string) and any(char in special_chars for char in string)]
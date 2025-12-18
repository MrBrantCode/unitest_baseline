"""
QUESTION:
Create a function named `replace_substring` that takes three parameters: `statement`, `substring`, and `new_substring`. The function should replace all instances of `substring` in `statement` with `new_substring` and return the resulting string. The function should be case-sensitive and replace all occurrences of `substring`, regardless of its position in `statement`.
"""

def replace_substring(statement, substring, new_substring):
    """
    Replaces all instances of substring in statement with new_substring and returns the resulting string.
    
    Args:
        statement (str): The original string.
        substring (str): The substring to be replaced.
        new_substring (str): The substring to replace with.
    
    Returns:
        str: The resulting string after replacement.
    """
    return statement.replace(substring, new_substring)
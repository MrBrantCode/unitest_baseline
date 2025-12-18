"""
QUESTION:
Implement a function `extract_substring` that takes two parameters: `original_string` and `length`. The function should return a substring of `original_string` with a maximum length of `length`. If `length` is greater than the length of `original_string`, the function should return the entire `original_string` without throwing an error.
"""

def extract_substring(original_string, length):
    """
    Extract a substring of `original_string` with a maximum length of `length`.

    Args:
        original_string (str): The string from which to extract the substring.
        length (int): The maximum length of the substring.

    Returns:
        str: A substring of `original_string` with a maximum length of `length`.
    """
    return original_string[:length]
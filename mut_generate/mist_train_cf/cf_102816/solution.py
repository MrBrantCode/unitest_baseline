"""
QUESTION:
Write a function `extract_characters(main_string, substring)` that takes two strings as input and returns a string containing all characters in `main_string` after the last occurrence of `substring`. The function should be case-sensitive and return an empty string if `substring` does not exist in `main_string`.
"""

def extract_characters(main_string, substring):
    """
    Extracts and returns all characters in main_string after the last occurrence of substring.

    Args:
        main_string (str): The string to extract characters from.
        substring (str): The substring to find the last occurrence of.

    Returns:
        str: A string containing all characters in main_string after the last occurrence of substring.
    """
    last_index = main_string.rfind(substring)
    
    if last_index == -1:
        return ""
    
    return main_string[last_index + len(substring):]
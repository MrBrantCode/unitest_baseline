"""
QUESTION:
Write a function `is_match(string, pattern)` that checks if a given string matches a specific pattern. The pattern can consist of two wildcard characters: '?' which matches any single character and '*' which matches any sequence of characters (including an empty sequence). The function should be case-sensitive.
"""

def is_match(string, pattern):
    """
    Checks if a given string matches a specific pattern.
    
    The pattern can consist of two wildcard characters: '?' which matches any single character 
    and '*' which matches any sequence of characters (including an empty sequence). 
    The function is case-sensitive.

    Args:
        string (str): The input string to be checked.
        pattern (str): The pattern to match against.

    Returns:
        bool: True if the string matches the pattern, False otherwise.
    """
    
    # Base case: if both the string and pattern are empty, they match
    if len(string) == 0 and len(pattern) == 0:
        return True
    
    # If the pattern is empty but the string is not, they don't match
    if len(pattern) == 0:
        return False
    
    # If the pattern starts with a "*", recursively check if the string
    # matches the pattern without the "*" or if the string matches the
    # pattern without the first character
    if pattern[0] == "*":
        return is_match(string, pattern[1:]) or (len(string) > 0 and is_match(string[1:], pattern))
    
    # If the pattern starts with a "?", recursively check if the string
    # matches the pattern without the "?" and the first character of string
    if pattern[0] == "?":
        return len(string) > 0 and is_match(string[1:], pattern[1:])
    
    # If the first characters of the string and pattern match, recursively
    # check if the remaining characters match
    return len(string) > 0 and string[0] == pattern[0] and is_match(string[1:], pattern[1:])
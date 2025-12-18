"""
QUESTION:
Create a function named `remove_substrings` that takes a string `s` as input. Remove all occurrences of "abcd" and "efgh" in a case-insensitive manner and return the resulting string. The removal should be case-insensitive, but the original case of the characters in the input string should be preserved.
"""

def remove_substrings(s):
    """
    Removes all occurrences of "abcd" and "efgh" in a case-insensitive manner.
    
    Args:
    s (str): The input string.
    
    Returns:
    str: The resulting string after removal.
    """
    s_lower = s.lower()
    s_lower = s_lower.replace("abcd", "").replace("efgh", "")
    return ''.join(c.upper() if s[i].isupper() else c for i, c in enumerate(s_lower))
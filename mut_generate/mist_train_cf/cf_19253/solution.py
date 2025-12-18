"""
QUESTION:
Create a function `remove_substrings` that takes a string `s` as input and returns the string with all occurrences of "abcd" and "efgh" removed in a case-insensitive manner. The original case of the remaining characters in the string should be preserved.
"""

def remove_substrings(s):
    """
    Removes all occurrences of "abcd" and "efgh" from a string in a case-insensitive manner.
    
    Args:
    s (str): The input string.
    
    Returns:
    str: The string with all occurrences of "abcd" and "efgh" removed.
    """
    
    # Convert s to lowercase for case-insensitive matching
    s_lower = s.lower()
    
    # Remove all occurrences of "abcd"
    s_lower = s_lower.replace("abcd", "")
    
    # Remove all occurrences of "efgh"
    s_lower = s_lower.replace("efgh", "")
    
    # Convert s_lower back to its original case
    s_new = ''.join(c.upper() if s[i].isupper() else c for i, c in enumerate(s_lower))
    
    return s_new
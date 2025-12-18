"""
QUESTION:
Write a function called `multi_replace` that takes a string and a list of tuples, where each tuple contains an old string and a new string. The function should return the modified string after replacing all occurrences of the old strings with the corresponding new strings.
"""

def multi_replace(s, substitutions):
    """
    This function replaces all occurrences of old strings with the corresponding new strings in a given string.
    
    Parameters:
    s (str): The original string to be modified.
    substitutions (list): A list of tuples containing the old string and the new string.
    
    Returns:
    str: The modified string after replacing all occurrences of the old strings with the corresponding new strings.
    """
    for old, new in substitutions:
        s = s.replace(old, new)
    return s
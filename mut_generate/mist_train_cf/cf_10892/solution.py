"""
QUESTION:
Write a function `extract_and_replace` that takes a string `s` and a character `c` as input. The function should return the substring of `s` that appears after the first occurrence of `c`, with all occurrences of `c` replaced with another character `new_c`. The original string `s` should be modified to replace all occurrences of `c` with `new_c` before extracting the substring.
"""

def extract_and_replace(s, c, new_c):
    """
    Extracts the substring of `s` that appears after the first occurrence of `c`, 
    with all occurrences of `c` replaced with `new_c`.

    Args:
        s (str): The original string.
        c (str): The character to replace.
        new_c (str): The character to replace with.

    Returns:
        str: The modified substring.
    """
    # Replace all occurrences of `c` with `new_c` in the original string
    modified_string = s.replace(c, new_c)
    
    # Find the index of the first occurrence of `new_c` (which was `c` before replacement)
    index = modified_string.find(new_c)
    
    # If `new_c` is not found, return an empty string
    if index == -1:
        return ""
    
    # Extract the substring after the first occurrence of `new_c`
    substring = modified_string[index + 1:]
    
    return substring
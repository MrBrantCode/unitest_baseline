"""
QUESTION:
Create a function `longest_common_prefix(str1, str2)` that takes two strings `str1` and `str2` as input, each with a minimum length of 5 characters. The function should find and return the longest common prefix between the two strings, ignoring special characters, spaces, and punctuation marks, and treating uppercase and lowercase letters as equal.
"""

import re

def longest_common_prefix(str1, str2):
    """
    Find and return the longest common prefix between two strings, 
    ignoring special characters, spaces, and punctuation marks, 
    and treating uppercase and lowercase letters as equal.

    Args:
    str1 (str): The first string with a minimum length of 5 characters.
    str2 (str): The second string with a minimum length of 5 characters.

    Returns:
    str: The longest common prefix between the two strings.
    """
    
    # Convert both strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # Remove special characters, spaces, and punctuation marks
    str1 = re.sub(r"[^a-z]", "", str1)
    str2 = re.sub(r"[^a-z]", "", str2)

    # Compare characters in the same position of both strings
    result = ""
    for i in range(min(len(str1), len(str2))):
        if str1[i] == str2[i]:
            result += str1[i]
        else:
            break

    return result
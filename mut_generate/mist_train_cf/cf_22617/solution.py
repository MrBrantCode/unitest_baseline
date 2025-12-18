"""
QUESTION:
Create a function called `concatenate_without_duplicates` that takes two strings as input and returns their concatenation without any duplicate characters. The function should not take any other inputs, and the order of characters in the resulting string should be the order of their first occurrence in the input strings.
"""

def concatenate_without_duplicates(str1, str2):
    """
    Concatenates two strings without any duplicate characters.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        str: The concatenated string without duplicates.
    """
    result = ""
    unique_chars = set()
    for c in str1 + str2:
        if c not in unique_chars:
            result += c
            unique_chars.add(c)
    return result
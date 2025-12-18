"""
QUESTION:
Create a function named `capitalize_concat` that takes two strings as input and returns their concatenation with the first letter of each word capitalized.
"""

def capitalize_concat(str1, str2):
    """
    This function takes two strings as input and returns their concatenation 
    with the first letter of each word capitalized.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        str: The concatenation of the two strings with the first letter of each word capitalized.
    """
    return str1.capitalize() + ' ' + str2.capitalize()
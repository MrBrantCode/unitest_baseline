"""
QUESTION:
Create a function `concatenate_strings(str1, str2)` that concatenates characters from `str1` that are also present in `str2`, ensuring each character appears only once in the resulting string and maintaining their original order from `str1`. The function should also remove any vowels (a, e, i, o, u) from the resulting string.
"""

def concatenate_strings(str1, str2):
    """
    Concatenates characters from `str1` that are also present in `str2`, 
    ensuring each character appears only once in the resulting string and 
    maintaining their original order from `str1`. The function also removes 
    any vowels (a, e, i, o, u) from the resulting string.

    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.

    Returns:
        str: The concatenated string.
    """
    concatenated_string = ""
    for char in str1:
        if char in str2 and char not in concatenated_string and char.lower() not in 'aeiou':
            concatenated_string += char
    return concatenated_string
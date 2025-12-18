"""
QUESTION:
Create a function `concat_and_capitalize` that takes two strings `str1` and `str2` as input and returns a new string that is the concatenation of `str1` and `str2` with the first letter capitalized. The function should have a time complexity of O(n), where n is the total length of `str1` and `str2`.
"""

def concat_and_capitalize(str1, str2):
    """
    Concatenates two input strings and capitalizes the first letter of the resulting string.

    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.

    Returns:
        str: The concatenated string with the first letter capitalized.
    """
    return (str1 + str2).capitalize()
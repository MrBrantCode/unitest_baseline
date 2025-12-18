"""
QUESTION:
Create a function `concat_unique_chars` that takes two strings as input and returns their concatenation without any duplicate characters. The resulting string should be sorted in alphabetical order. The function should not take any other parameters and should return a string.
"""

def concat_unique_chars(str1, str2):
    """
    Concatenates two strings without any duplicate characters and returns the result in alphabetical order.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        str: The concatenated string without duplicates, sorted in alphabetical order.
    """
    unique_chars = set()
    result = "".join(c for c in str1 + str2 if not (c in unique_chars or unique_chars.add(c)))
    return ''.join(sorted(result))
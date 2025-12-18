"""
QUESTION:
Write a function `compareStrings` that takes two strings `str1` and `str2` as input and returns a string indicating which input string has more unique characters. If both strings have the same number of unique characters, the function should return a message stating this. Additionally, implement a function `countUniqueCharacters` that takes a string `str` as input and returns a dictionary where the keys are unique characters in the string and the values are their respective counts.
"""

def compareStrings(str1, str2):
    """
    Compare two strings and determine which string has more unique characters.

    Args:
    str1 (str): The first string to compare.
    str2 (str): The second string to compare.

    Returns:
    str: A message indicating which string has more unique characters or if both strings have the same number of unique characters.
    """
    uniqueChars1 = set(str1)
    uniqueChars2 = set(str2)

    if len(uniqueChars1) > len(uniqueChars2):
        return f"'{str1}' has more unique characters."
    elif len(uniqueChars2) > len(uniqueChars1):
        return f"'{str2}' has more unique characters."
    else:
        return "Both strings have the same number of unique characters."


def countUniqueCharacters(str):
    """
    Count the occurrence of each unique character in a string.

    Args:
    str (str): The input string.

    Returns:
    dict: A dictionary where the keys are unique characters in the string and the values are their respective counts.
    """
    charCount = {}

    for char in str:
        if char in charCount:
            charCount[char] += 1
        else:
            charCount[char] = 1

    return charCount
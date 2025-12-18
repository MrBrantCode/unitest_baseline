"""
QUESTION:
Write a function `most_common_char` that takes a string as input and returns the character that appears most frequently in the string.
"""

def most_common_char(string):
    """
    This function returns the character that appears most frequently in the input string.

    Args:
    string (str): The input string.

    Returns:
    str: The most common character in the string.
    """
    string_lower = string.replace(' ', '').lower()
    freq = {}
    for char in string_lower:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    most_common = max(freq, key=freq.get)
    return most_common
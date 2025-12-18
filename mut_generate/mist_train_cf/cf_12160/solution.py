"""
QUESTION:
Write a function named most_frequent_character that takes a string as input, considers only alphabetic characters, and ignores letter case. Return the most frequent character in the string.
"""

def most_frequent_character(s):
    """
    Returns the most frequent alphabetic character in a given string, ignoring case.

    Args:
        s (str): Input string.

    Returns:
        str: The most frequent alphabetic character in the string.
    """
    s = ''.join(filter(str.isalpha, s)).lower()
    if not s:
        return ''
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return max(freq, key=freq.get)
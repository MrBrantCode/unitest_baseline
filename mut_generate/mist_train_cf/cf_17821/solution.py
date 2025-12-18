"""
QUESTION:
Design a function `remove_punctuation_and_duplicates` that takes a string and a punctuation mark as input, removes all occurrences of the punctuation mark, and removes any adjacent duplicate characters in the resulting string. The function should return the modified string.
"""

def remove_punctuation_and_duplicates(s, punctuation):
    """
    Removes all occurrences of the punctuation mark and any adjacent duplicate characters in the string.

    Args:
        s (str): The input string.
        punctuation (str): The punctuation mark to be removed.

    Returns:
        str: The modified string.
    """
    modified_string = []
    for i, char in enumerate(s):
        if char == punctuation:
            continue
        if i > 0 and char == s[i-1]:
            continue
        modified_string.append(char)
    return ''.join(modified_string)
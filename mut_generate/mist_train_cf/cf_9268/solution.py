"""
QUESTION:
Write a function named `replace_key` that takes a string and two parameters, `key` and `value`, and replaces all occurrences of the `key` with the `value` in the string. The replacement should only occur when the `key` is a separate word, not as a substring of other words.
"""

def replace_key(string, key, value):
    """
    Replaces all occurrences of the key with the value in the string.
    The replacement only occurs when the key is a separate word, not as a substring of other words.

    Args:
        string (str): The input string.
        key (str): The word to be replaced.
        value (str): The replacement value.

    Returns:
        str: The modified string.
    """
    words = string.split()
    for i in range(len(words)):
        if words[i] == key:
            words[i] = value
    return ' '.join(words)
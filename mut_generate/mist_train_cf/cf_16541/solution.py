"""
QUESTION:
Develop a function named `unique_chars` that takes a string as input and returns the number of unique characters in the string, ignoring case sensitivity, without using any additional data structures.
"""

def unique_chars(s):
    """
    Returns the number of unique characters in the string, ignoring case sensitivity.

    Args:
        s (str): The input string.

    Returns:
        int: The number of unique characters.
    """
    lower_str = s.lower()
    count = 0

    for i in range(len(lower_str)):
        is_unique = True
        for j in range(i):
            if lower_str[i] == lower_str[j]:
                is_unique = False
                break
        if is_unique:
            count += 1

    return count
"""
QUESTION:
Write a function `find_indexes(strings, target)` that takes a list of strings and a target string, and returns the indices of two strings in the list whose combined length is equal to the length of the target string. Assume that there is exactly one distinct solution and that no string can be used twice.
"""

def find_indexes(strings, target):
    """
    Returns the indices of two strings in the list whose combined length is equal to the length of the target string.

    Args:
        strings (list): A list of strings.
        target (str): The target string.

    Returns:
        list: A list containing the indices of two strings whose combined length equals the length of the target string. 
              If no such pair is found, returns None.
    """
    len_target = len(target)
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) + len(strings[j]) == len_target:
                return [i, j]
    return None
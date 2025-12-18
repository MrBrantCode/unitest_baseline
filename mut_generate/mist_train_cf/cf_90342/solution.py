"""
QUESTION:
Transform each string in a given list to upper case, remove duplicates, and sort the resulting list in descending order by string length. The list may contain strings with special characters and numbers. The function should be named `process_strings`.
"""

def process_strings(strings):
    """
    This function transforms each string in a given list to upper case, removes duplicates, 
    and sorts the resulting list in descending order by string length.

    Args:
        strings (list): A list of strings.

    Returns:
        list: A list of strings in upper case with duplicates removed, sorted in descending order by string length.
    """
    strings = [string.upper() for string in strings]
    strings = list(set(strings))
    strings.sort(reverse=True, key=len)
    return strings
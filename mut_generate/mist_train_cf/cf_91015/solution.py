"""
QUESTION:
Write a function `find_subsequence_index(string, integer)` that takes a string and an integer as input, and returns the index of the first occurrence of a specific subsequence of characters in the string. The subsequence consists of the digits in the integer concatenated in ascending order. If the subsequence is not found, return -1.
"""

def find_subsequence_index(string, integer):
    """
    Returns the index of the first occurrence of a specific subsequence of characters in the string.
    The subsequence consists of the digits in the integer concatenated in ascending order.
    If the subsequence is not found, return -1.

    Args:
        string (str): The string to search for the subsequence.
        integer (int): The integer from which the subsequence is derived.

    Returns:
        int: The index of the first occurrence of the subsequence, or -1 if not found.
    """
    subsequence = ''.join(sorted(str(integer)))
    index = string.find(subsequence)
    return index
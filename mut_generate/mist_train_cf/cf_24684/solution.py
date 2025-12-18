"""
QUESTION:
Design a function called `check_permutation` that takes two string parameters, `str1` and `str2`, as input and returns a boolean value indicating whether they are permutations of each other.
"""

def check_permutation(str1, str2):
    """
    Checks if two input strings are permutations of each other.

    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.

    Returns:
        bool: True if the strings are permutations of each other, False otherwise.
    """
    # If the lengths of the strings are not equal, they cannot be permutations
    if len(str1) != len(str2):
        return False

    # Sort the characters in each string and compare the results
    return sorted(str1) == sorted(str2)
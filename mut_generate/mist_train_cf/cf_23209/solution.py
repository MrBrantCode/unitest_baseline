"""
QUESTION:
Write a function `compare_strings` that takes two strings as input and returns `True` if they are equal (ignoring leading and trailing white spaces) and `False` otherwise. The function should have a time complexity of O(n), where n is the length of the longer string after removing leading and trailing white spaces, and a space complexity of O(1).
"""

def compare_strings(string_1, string_2):
    """
    Compare two strings for equality, ignoring leading and trailing white spaces.

    Args:
    string_1 (str): The first string to compare.
    string_2 (str): The second string to compare.

    Returns:
    bool: True if the strings are equal, False otherwise.
    """

    # Remove leading and trailing white spaces
    string_1 = string_1.strip()
    string_2 = string_2.strip()

    # Compare the lengths of the strings
    if len(string_1) != len(string_2):
        return False

    # Compare each character of the strings
    for i in range(len(string_1)):
        if string_1[i] != string_2[i]:
            return False

    return True
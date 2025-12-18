"""
QUESTION:
Write a function `compare_string_lengths` that takes two strings as input and prints out the longer string. The function should not use any built-in functions or libraries that directly determine the length of the strings. The time complexity should be O(n), where n is the length of the longer string.
"""

def compare_string_lengths(str1, str2):
    """
    This function compares the lengths of two input strings without using built-in length functions.
    It then returns the longer string.

    Parameters:
    str1 (str): The first input string.
    str2 (str): The second input string.

    Returns:
    str: The longer string.
    """
    # Initialize variables to keep track of the length of each string
    len1 = 0
    len2 = 0

    # Iterate over the characters in the first string
    for char in str1:
        # Increment the length counter
        len1 += 1

    # Iterate over the characters in the second string
    for char in str2:
        # Increment the length counter
        len2 += 1

    # Compare the lengths of the two strings
    if len1 >= len2:
        return str1
    else:
        return str2
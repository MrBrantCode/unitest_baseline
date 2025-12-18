"""
QUESTION:
Create a function `findPattern` that takes two strings as parameters and returns 1 if the second string is a subsequence of the first string, otherwise 0. The length of the first string is between 1 and 10^5, and the length of the second string is between 1 and the length of the first string.
"""

def findPattern(s1, s2):
    """
    This function checks if the second string is a subsequence of the first string.

    Parameters:
    s1 (str): The main string.
    s2 (str): The string to be checked.

    Returns:
    int: 1 if s2 is a subsequence of s1, 0 otherwise.
    """
    i = j = 0  # Initialize two pointers at the beginning of each string
    while i < len(s1) and j < len(s2):  # Continue until we reach the end of either string
        if s1[i] == s2[j]:  # If the characters at the current positions match
            j += 1  # Move the pointer for the second string to the right
        i += 1  # Move the pointer for the first string to the right
    return 1 if j == len(s2) else 0  # Return 1 if we reached the end of the second string, 0 otherwise
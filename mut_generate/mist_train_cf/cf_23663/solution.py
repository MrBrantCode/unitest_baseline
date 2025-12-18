"""
QUESTION:
Write a function `num_substrings` that calculates the total number of possible substrings for a given string `S`. The function should return an integer representing the total count of substrings. The input string `S` only contains lowercase English letters.
"""

def num_substrings(S):
    """
    This function calculates the total number of possible substrings for a given string S.

    Args:
    S (str): The input string containing only lowercase English letters.

    Returns:
    int: The total count of substrings.

    """
    result = 0
    n = len(S)
    for i in range(n):
        # Calculate the number of possible substrings for each prefix of S
        result += (i + 1)
    return result
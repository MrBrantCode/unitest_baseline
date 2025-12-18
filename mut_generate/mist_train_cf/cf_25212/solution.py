"""
QUESTION:
Write a function called `longest_common_substring` that takes two strings as input and returns the longest common substring between them. The function should be able to handle strings of any length.
"""

def longest_common_substring(s1, s2):
    """
    This function finds the longest common substring between two input strings.

    Args:
        s1 (str): The first input string.
        s2 (str): The second input string.

    Returns:
        str: The longest common substring between s1 and s2.
    """

    # Initialize a 2D array to store the lengths of common substrings
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    # Initialize variables to store the maximum length and the ending position of the longest common substring
    max_length = 0
    end = 0

    # Iterate over the characters in both strings
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            # If the current characters in both strings are equal, update the length of the common substring
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                # Update the maximum length and ending position if a longer common substring is found
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end = i
            # If the current characters are not equal, reset the length of the common substring
            else:
                dp[i][j] = 0

    # Return the longest common substring
    return s1[end - max_length: end]
"""
QUESTION:
Write a function named `longest_common_substring` that takes two strings, `s1` and `s2`, as input and returns the longest common substring between them. The strings may contain uppercase and lowercase letters, numbers, and special characters. The function should return the longest common substring without any additional information.
"""

def longest_common_substring(s1, s2):
    """
    Returns the longest common substring between two input strings.

    Args:
    s1 (str): The first input string.
    s2 (str): The second input string.

    Returns:
    str: The longest common substring between s1 and s2.
    """

    # Initialize a 2D table to store the lengths of common substrings
    table = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    # Track the length and ending position of the longest common substring
    max_length = 0
    ending_pos = 0

    # Fill the table using dynamic programming
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
                if table[i][j] > max_length:
                    max_length = table[i][j]
                    ending_pos = i
            else:
                table[i][j] = 0

    # Extract the longest common substring
    longest_substring = s1[ending_pos - max_length:ending_pos]

    return longest_substring
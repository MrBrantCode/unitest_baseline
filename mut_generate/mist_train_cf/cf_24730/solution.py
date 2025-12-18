"""
QUESTION:
Write a function `longest_run` that takes a string as input and returns the length of the longest run of consecutive repeated characters. The function should return the maximum length of a sequence of the same character.
"""

def longest_run(s):
    """
    Returns the length of the longest run of consecutive repeated characters in a string.

    Args:
        s (str): The input string.

    Returns:
        int: The length of the longest run of consecutive repeated characters.
    """
    if not s:  # edge case: empty string
        return 0

    max_run_length = 1
    current_run_length = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_run_length += 1
        else:
            max_run_length = max(max_run_length, current_run_length)
            current_run_length = 1

    return max(max_run_length, current_run_length)
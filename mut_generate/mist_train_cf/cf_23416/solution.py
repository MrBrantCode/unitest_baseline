"""
QUESTION:
Write a function called `length_of_longest_substring` that takes a string as input and returns the length of the longest substring. The input string may contain any characters, including letters, numbers, and special characters. The function should return the length of the longest substring in the input string.
"""

def length_of_longest_substring(s: str) -> int:
    """
    Returns the length of the longest substring in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The length of the longest substring.
    """
    if not s:
        return 0

    max_length = start = 0
    used_chars = {}

    for i, char in enumerate(s):
        if char in used_chars and start <= used_chars[char]:
            start = used_chars[char] + 1
        else:
            max_length = max(max_length, i - start + 1)

        used_chars[char] = i

    return max_length
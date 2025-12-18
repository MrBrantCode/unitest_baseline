"""
QUESTION:
Write a function named `count_unique_chars` that takes a string `s` as input and returns the number of unique characters in the string, ignoring case sensitivity. The function should have a time complexity of O(n), where n is the length of the string, and use a constant amount of space. Do not use any built-in functions or methods for string manipulation or character counting, and assume that the input string only contains English alphabet characters.
"""

def count_unique_chars(s):
    """
    Returns the number of unique characters in the string, ignoring case sensitivity.

    Args:
        s (str): The input string.

    Returns:
        int: The number of unique characters in the string.
    """
    count = 0
    visited = [False] * 26

    s = s.lower()

    for c in s:
        index = ord(c) - ord('a')
        if not visited[index]:
            count += 1
            visited[index] = True

    return count
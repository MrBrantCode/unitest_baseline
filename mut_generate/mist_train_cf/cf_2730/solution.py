"""
QUESTION:
Given a string of length n, write a function `count_distinct_substrings` that returns the number of distinct continuous substrings in the string, where a distinct substring is defined as a substring that does not contain any duplicate characters. The input string can contain uppercase and lowercase letters, digits, and special characters, and has a length of 1 ≤ n ≤ 10^6. The solution must have a time complexity of O(n^2) and a space complexity of O(n), using only constant extra space (excluding the input and output variables), and without using any built-in data structures or libraries for handling strings or arrays.
"""

def count_distinct_substrings(s):
    """
    Returns the number of distinct continuous substrings in the input string.

    Args:
        s (str): The input string.

    Returns:
        int: The number of distinct continuous substrings.
    """

    count = 0
    window_start = 0
    char_set = set()

    for window_end in range(len(s)):
        while s[window_end] in char_set:
            char_set.remove(s[window_start])
            window_start += 1

        char_set.add(s[window_end])
        count += window_end - window_start + 1

    return count
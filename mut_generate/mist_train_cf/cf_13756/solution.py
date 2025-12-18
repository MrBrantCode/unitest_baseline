"""
QUESTION:
Determine if a set of strings is a palindrome. The set contains only lowercase or uppercase English alphabets and the maximum length of each string is 100. The palindrome test is case-insensitive. Write a function `is_palindrome_set` that takes a set of strings as input and returns a boolean value indicating whether the set is a palindrome.
"""

def is_palindrome_set(s):
    """
    Determine if a set of strings is a palindrome. The set contains only lowercase 
    or uppercase English alphabets and the maximum length of each string is 100. 
    The palindrome test is case-insensitive.

    Args:
        s (set): A set of strings.

    Returns:
        bool: True if the set is a palindrome, False otherwise.
    """
    reversed_set = set()
    for string in s:
        lower_str = string.lower()
        reversed_str = lower_str[::-1]
        reversed_set.add(reversed_str)
    return s == {string.lower() for string in reversed_set}
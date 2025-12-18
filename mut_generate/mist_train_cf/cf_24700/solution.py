"""
QUESTION:
Write a function `findLongestPalindrome(str)` that finds the longest palindrome substring in a given string `str`. A palindrome is a string that reads the same backwards as forwards. The function should return the longest palindrome substring. The input string `str` may contain spaces and punctuation.
"""

def findLongestPalindrome(s):
    """
    Finds the longest palindrome substring in a given string.

    Args:
        s (str): The input string.

    Returns:
        str: The longest palindrome substring.
    """
    longest_palindrome = ''

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            current_substr = s[i:j]

            if current_substr == current_substr[::-1] and len(current_substr) > len(longest_palindrome):
                longest_palindrome = current_substr

    return longest_palindrome
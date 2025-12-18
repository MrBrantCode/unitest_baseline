"""
QUESTION:
Write a recursive function `reverse_string(s: str) -> str` that reverses the input string `s` without using any built-in string reversal functions or methods. The input string `s` is guaranteed to have a length between 1 and 10^5 and only contain printable ASCII characters.
"""

def reverse_string(s: str) -> str:
    if len(s) <= 1:
        return s
    else:
        return reverse_string(s[1:]) + s[0]
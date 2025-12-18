"""
QUESTION:
Write a recursive function `reverse_string(s: str) -> str` that takes a string `s` with a length between 1 and 10^5 as input and returns a string which is the reverse of the input string. The function must not use any built-in string reversal functions or methods. The input string will only contain printable ASCII characters.
"""

def entance(s: str) -> str:
    if len(s) <= 1:
        return s
    else:
        return entance(s[1:]) + s[0]
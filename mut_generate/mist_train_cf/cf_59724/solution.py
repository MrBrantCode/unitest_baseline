"""
QUESTION:
Create the `magic_or_mundane(s, t)` function. Given a string `s` of lowercase English alphabets and a target number `t`, determine if the sequence is magical. A magical sequence is one where the sum of each alphabet's position in the English alphabet equals `t` and the sequence is a palindrome. The function should be optimized for longer strings.
"""

def magic_or_mundane(s, t):
    def is_palindrome(s):
        return s == s[::-1]

    def get_val(s):
        return sum(ord(c) - ord('a') + 1 for c in s)

    return is_palindrome(s) and get_val(s) == t
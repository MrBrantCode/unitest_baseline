"""
QUESTION:
Implement the `magic_or_mundane` function, which determines whether a given string `s` of lowercase English alphabets is magical. A magical sequence must meet three conditions: it is a palindrome, it does not contain consecutive repeated alphabets, and the sum of each alphabet's position in the alphabet equals the target number `t`.
"""

def magic_or_mundane(s, t):
    if s != s[::-1]:
        return False

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False

    if sum([ord(i) - ord('a') + 1 for i in s]) != t:
        return False

    return True
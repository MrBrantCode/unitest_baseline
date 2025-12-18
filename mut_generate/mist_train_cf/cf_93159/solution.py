"""
QUESTION:
Implement a function `remove_occurrences(s, t)` that removes all occurrences of string `t` from string `s` in a case-sensitive manner. The function should return the modified string `s` with all occurrences of `t` removed.
"""

def remove_occurrences(s, t):
    result = ""
    i = 0
    while i < len(s):
        if s[i:i+len(t)] == t:
            i += len(t)
        else:
            result += s[i]
            i += 1
    return result
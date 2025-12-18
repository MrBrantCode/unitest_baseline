"""
QUESTION:
Implement the function `find_pattern_index` that takes two parameters: a string `s` and a pattern `p`. The function should return the first index of the pattern `p` in the string `s`. The pattern `p` can contain the following wildcards: '*' to match any sequence of characters (including an empty sequence), '?' to match any single character, and '+' to match any single digit character.
"""

def find_pattern_index(s, p):
    def match(s, p, s_index, p_index):
        if p_index == len(p):
            return s_index == len(s)
        if p[p_index] == '*':
            return any(match(s, p, i, p_index + 1) for i in range(s_index, len(s) + 1))
        if s_index >= len(s):
            return False
        if p[p_index] == '?':
            return match(s, p, s_index + 1, p_index + 1)
        if p[p_index] == '+':
            return s[s_index].isdigit() and match(s, p, s_index + 1, p_index + 1)
        return s[s_index] == p[p_index] and match(s, p, s_index + 1, p_index + 1)

    for i in range(len(s)):
        if match(s, p, i, 0):
            return i
    return -1
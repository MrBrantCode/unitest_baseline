"""
QUESTION:
Write a function `isIsomorphic(s: str, t: str) -> bool` that determines if two strings `s` and `t` are isomorphic under the condition that the frequency of each character in `s` is the same as the frequency of the corresponding character in `t`. `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t` while preserving the order of characters, and no two characters may map to the same character, but a character may map to itself. The function should take two parameters `s` and `t` with the following constraints: `1 <= s.length <= 5 * 10^4`, `t.length == s.length`, and `s` and `t` consist of any valid ASCII characters.
"""

def isIsomorphic(s: str, t: str) -> bool:
    s_to_t = {}
    t_to_s = {}
    for c_s, c_t in zip(s, t):
        if (c_s in s_to_t and s_to_t[c_s] != c_t) or (c_t in t_to_s and t_to_s[c_t] != c_s):
            return False
        s_to_t[c_s] = c_t
        t_to_s[c_t] = c_s
    return True
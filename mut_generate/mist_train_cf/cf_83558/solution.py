"""
QUESTION:
Write a function `isIsomorphic(s: str, t: str) -> bool` that determines if two strings `s` and `t` are isomorphic under the condition that the frequency of each character in `s` is the same as the frequency of the corresponding character in `t` and the relative positions of the characters in `s` and `t` are the same. The function should return `True` if `s` and `t` are isomorphic, `False` otherwise.

Restrictions: `1 <= s.length <= 5 * 104`, `t.length == s.length`, and `s` and `t` consist of any valid ascii character.
"""

def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    map_s = {}
    map_t = {}
    for i in range(len(s)):
        if s[i] not in map_s:
            map_s[s[i]] = t[i]
        if t[i] not in map_t:
            map_t[t[i]] = s[i]
        if map_t[t[i]] != s[i] or map_s[s[i]] != t[i]:
            return False
    return True
"""
QUESTION:
Write a Python function `is_isomorphic(s, t)` that determines if two input strings `s` and `t` are isomorphic. The function should ensure the mapping between characters in `s` and `t` is bijective, i.e., each character in `s` maps to exactly one character in `t` and vice versa. The function should handle non-ASCII characters, uppercase and lowercase letters as separate entities, whitespace, and punctuation symbols.
"""

def is_isomorphic(s, t): 
    map_s_t = {}
    map_t_s = {}
    for char_s, char_t in zip(s, t):
        if char_s not in map_s_t and char_t not in map_t_s:
            map_s_t[char_s] = char_t
            map_t_s[char_t] = char_s
        elif map_s_t.get(char_s) != char_t or map_t_s.get(char_t) != char_s:
            return False
    return True
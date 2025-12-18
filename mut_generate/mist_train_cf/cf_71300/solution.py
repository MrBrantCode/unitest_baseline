"""
QUESTION:
Create a function `is_isomorphic(s, t)` that checks if two given strings `s` and `t` are isomorphic to each other. The function should return `True` if the strings are isomorphic and `False` otherwise. The strings can be empty or contain spaces and special characters. The function should have a time complexity of less than O(n^2), where n is the length of the string.
"""

def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for char_s, char_t in zip(s, t):
        if char_s not in s_to_t and char_t not in t_to_s:
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s
        elif char_s not in s_to_t or s_to_t[char_s] != char_t or t_to_s[char_t] != char_s:
            return False

    return True
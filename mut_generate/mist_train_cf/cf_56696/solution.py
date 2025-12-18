"""
QUESTION:
Implement a function `is_isomorphic(s, t)` that determines if two input strings `s` and `t` are isomorphic. The function should return `True` if the strings are isomorphic and `False` otherwise. The function should handle all possible Unicode characters, not just lowercase English alphabets, and should be efficient enough to handle strings of length up to 10^6 characters. The function should not use any built-in functions beyond the built-in features of Python data structures.
"""

def is_isomorphic(s, t):
    map_s_t = {}  
    map_t_s = {}  

    if len(s) != len(t):
        return False

    for c_s, c_t in zip(s, t):
        if c_s in map_s_t:
            if map_s_t[c_s] != c_t:
                return False
        if c_t in map_t_s:
            if map_t_s[c_t] != c_s:
                return False
            
        map_s_t[c_s] = c_t
        map_t_s[c_t] = c_s
    return True
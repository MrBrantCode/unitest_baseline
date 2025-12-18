"""
QUESTION:
Write a Python function `isIsomorphic(s: str, t: str) -> bool` that determines if two input strings `s` and `t` are isomorphic, meaning they have the same character substitution pattern. The function should not use any built-in functions. It should return `True` if the strings are isomorphic and `False` otherwise. The function should handle cases where characters may be isomorphic in a one-way sense but not in a two-way sense.
"""

def isIsomorphic(s: str, t: str) -> bool:
    dic1, dic2 = {}, {}
    for i, value in enumerate(s):
        dic1[value] = dic1.get(value, []) + [i]
    for i, value in enumerate(t):
        dic2[value] = dic2.get(value, []) + [i]
    return sorted(dic1.values()) == sorted(dic2.values())
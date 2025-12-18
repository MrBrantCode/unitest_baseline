"""
QUESTION:
Write a function `is_rotation(s1, s2)` that determines whether two strings `s1` and `s2` have a rotational relationship, meaning that `s2` can be derived from `s1` via rotation. The function should return `True` if `s1` and `s2` are rotations of each other, and `False` otherwise. The function should not use any additional data structures and should have a time complexity of O(n), where n is the length of the strings.
"""

def is_rotation(s1, s2):
    if len(s1) != len(s2):  
        return False

    s1_twice = s1 + s1  

    if s2 in s1_twice:  
        return True
    else:
        return False
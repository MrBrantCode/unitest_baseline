"""
QUESTION:
Given two strings `s` and `t` containing lowercase letters and '@' characters, write a function named `compareUndo` that returns `True` if the strings are equal after applying '@' as an undo operation, which removes the last two characters, and `False` otherwise. The function should run in `O(n)` time and use `O(1)` space. The length of `s` and `t` is between 1 and 200.
"""

def compareUndo(s, t):
    """Returns True if strings s and t are equal after applying '@' as an undo operation."""
    def undo(compare):
        res = []
        for c in compare:
            if c != '@':
                res.append(c)
            elif res:
                res.pop()
        return ''.join(res)
    
    return undo(s) == undo(t)
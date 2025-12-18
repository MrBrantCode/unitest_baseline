"""
QUESTION:
Write a function `isLongPressedName(name: str, typed: str) -> bool` to determine if it's possible that `typed` was your friend's name with some characters being long pressed or extra characters being added. The function should return `True` if it is possible, and `False` otherwise. The constraints are: `1 <= name.length <= 1000`, `1 <= typed.length <= 1000`, and both `name` and `typed` contain only lowercase English letters.
"""

def isLongPressedName(name: str, typed: str) -> bool:
    i = j = 0
    while i < len(name) and j < len(typed):
        if name[i] == typed[j]:
            i += 1
            j += 1
        elif j > 0 and typed[j] == typed[j - 1]:
            j += 1
        else:
            return False
    while j < len(typed) and typed[j] == typed[j - 1]: 
        j += 1
    return i == len(name) and j == len(typed)
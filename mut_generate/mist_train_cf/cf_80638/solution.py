"""
QUESTION:
Write a function `monotonic(l: list, strict: bool = False)` that checks whether the given list `l` is monotonic. A list is considered monotonic if it is either entirely non-increasing or non-decreasing. If `strict` is `True`, the list should not have any equal consecutive items. The function should return `True` if the list is monotonic and `False` otherwise.
"""

def entrance(l: list, strict: bool = False):
    if len(l) < 2:
        return True  
    dir = l[1] - l[0]  
    for i in range(2, len(l)):
        if not dir:  
            dir = l[i] - l[i - 1]
        if strict and dir == 0:  
            return False
        if dir > 0:
            if l[i] - l[i - 1] < 0:  
                return False
        elif strict and l[i] - l[i - 1] <= 0:  
            return False
        if dir < 0:
            if l[i] - l[i - 1] > 0:  
                return False
        elif strict and l[i] - l[i - 1] >= 0:  
            return False
    return True
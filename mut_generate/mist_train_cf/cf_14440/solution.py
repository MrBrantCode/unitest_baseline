"""
QUESTION:
Write a function `xor(a, b)` that returns the logical XOR between two given boolean variables `a` and `b`. The function should handle the case when either or both of the input variables are `None`.
"""

def xor(a, b):
    if a is None and b is None:  
        return None
    elif a is None:  
        return b
    elif b is None:  
        return a
    else:  
        return a != b
"""
QUESTION:
Create a function called `xor(a, b)` that takes two boolean variables `a` and `b` as input and returns their logical XOR. The function should also handle cases where either or both of `a` and `b` are `None`, and return the corresponding result.
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
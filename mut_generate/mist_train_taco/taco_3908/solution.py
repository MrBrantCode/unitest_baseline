"""
QUESTION:
Reverse and invert all integer values in a given list. 

Python:

    reverse_invert([1,12,'a',3.4,87,99.9,-42,50,5.6]) = [-1,-21,-78,24,-5]
    
Ignore all other types than integer.
"""

def reverse_invert_integers(lst):
    from math import copysign as sign
    
    return [-int(sign(int(str(abs(x))[::-1]), x)) for x in lst if isinstance(x, int)]
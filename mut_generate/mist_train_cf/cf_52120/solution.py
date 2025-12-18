"""
QUESTION:
Implement a function `rotate_string(A, B)` that checks if string `A` can be rotated to become string `B` through a series of left shifts. The function should return a tuple of two values: a boolean indicating whether `A` can become `B` through shifts, and the minimum number of shifts required to transform `A` into `B` if possible, or -1 if not possible.

The function should consider circular shifts, where shifting off the end of the string wraps around to the beginning. Strings `A` and `B` will have length at most 100.
"""

def rotate_string(A, B):
    if len(A) != len(B):
        return False, -1
    
    # check for circular string
    if B in A+A:
        for i in range(len(A)):
            if A[i:] + A[:i] == B:
                return True, i
            
    return False, -1
"""
QUESTION:
Write a function `check_overflow(n)` that checks if a given integer `n` exceeds the maximum integer size allowed by the system. The function should return `True` if `n` overflows and `False` otherwise. The function should be implemented in Python and should use the `sys` module to get the maximum integer size.
"""

import sys

def check_overflow(n): 
    return n > sys.maxsize
"""
QUESTION:
Create a function `f` that takes an integer `n` and returns a list of size `n`. The value at index `i` (1-indexed) should be the factorial of `i` if `i` is even, and the summation of all numbers from 1 to `i` if `i` is odd. The function should not use any loops or recursion.
"""

from math import factorial
from functools import reduce
from operator import add

def f(n):
    if n==0: 
        return []
    return [factorial(i) if i%2 == 0 else reduce(add,range(1,i+1)) for i in range(1,n+1)]
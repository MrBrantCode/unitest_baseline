"""
QUESTION:
Implement the function `tribonacci(n)` to return the `n`-th Tribonacci number, where `Tn+3 = Tn + Tn+1 + Tn+2` for `n >= 0`, given the initial conditions `T0 = 0`, `T1 = 1`, and `T2 = 1`. The function must not use any form of loop (for, while, do-while) or recursion without using memoization or caching. The input `n` is in the range `0 <= n <= 37`, and the output will fit within a 32-bit integer.
"""

from functools import lru_cache

@lru_cache(None)
def tribonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
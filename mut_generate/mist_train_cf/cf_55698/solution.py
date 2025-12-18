"""
QUESTION:
Given a positive integer `n` where `1 <= n < 2^31 - 1`, write a function `is_blissful` to determine if `n` is a blissful number, which is defined as a number that eventually becomes 1 by repeatedly replacing it with the sum of the squares of its digits. If `n` becomes 1, return `True`; otherwise, return `False`.
"""

def is_blissful(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(i)**2 for i in str(n))
    return n == 1
"""
QUESTION:
Create a function `convert_all_sums(n, m, start, base)` that calculates the sum of numbers from `n` to `m` (inclusive), adds a starting number `start`, and converts the sum into a custom base system. The function should take four parameters: two positive integers `n` and `m` where `n <= m`, an integer `start`, and an integer `base` ranging from 2 to 10. If `n > m`, `start < 0`, or `base` is out of range, return -1.
"""

def convert_all_sums(n, m, start, base):
    if n > m or start < 0 or not(2 <= base <= 10):
        return -1
    total = sum(range(n, m+1)) + start
    if base == 2:
        return bin(total)
    elif base == 8:
        return oct(total)
    elif base == 10:
        return str(total)
    else:
        return "Base not supported"
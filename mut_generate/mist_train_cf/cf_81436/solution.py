"""
QUESTION:
Write a function `reorderedPowerOf2(n)` that takes an integer `n` as input and returns `True` if the digits of `n` can be rearranged to form a power of 2, and `False` otherwise. The input integer `n` is within the range `1 <= n <= 10^9`.
"""

def can_reorder_power_of_2(n):
    return sorted(str(n)) in [sorted(str(1<<i)) for i in range(31)]
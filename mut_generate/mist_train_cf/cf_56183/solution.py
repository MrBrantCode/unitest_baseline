"""
QUESTION:
Create a function named `monotonic` that takes a list of integers `l` and an optional boolean parameter `strict` (defaulting to `False`) and returns `True` if the list elements are monotonically increasing or decreasing, considering the strictness requirement, and `False` otherwise. The list must not contain any prime numbers. If `strict` is `True`, adjacent elements must differ; otherwise, they may be equal.
"""

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqr = int(n**0.5) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def is_monotonic(l: list, strict: bool = False) -> bool:
    if any(is_prime(x) for x in l):
        return False
    if strict:
        return all(x < y for x, y in zip(l, l[1:])) or all(x > y for x, y in zip(l, l[1:]))
    else:
        return all(x <= y for x, y in zip(l, l[1:])) or all(x >= y for x, y in zip(l, l[1:]))
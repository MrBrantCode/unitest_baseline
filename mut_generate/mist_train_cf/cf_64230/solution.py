"""
QUESTION:
Define a function `smallest_with_same_tree` that calculates the smallest number `M(n)` which has a factor tree identical in shape to the factor tree for `n!!` (double factorial of `n`), given an integer `n > 1`. The function should use a binary factor tree `T(n)` constructed based on the following rules: if `n` is a prime number, `T(n)` is a tree with a single node `n`; if `n` is not a prime number, `T(n)` is a binary tree with root node `n`, left subtree `T(a)`, and right subtree `T(b)`, where `a` and `b` are positive integers such that `n = ab`, `a <= b`, and `b - a` is minimized.
"""

import math

def smallest_with_same_tree(n):
    c = 3 
    while True:
        if factor_tree(n) == factor_tree(c):
            return c
        c += 1

def factor_tree(n):
    factors = []
    while n % 2 == 0: 
        factors.append(2)
        n //= 2
    i = 3
    while i * i <= n: 
        if n % i:
            i += 2
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return sorted([i for i in factors], reverse=True)
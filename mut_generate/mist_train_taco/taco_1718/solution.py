"""
QUESTION:
In this Kata, you will be given two numbers, `a` and `b`, and your task is to determine if the first number `a` is divisible by `all` the prime factors of the second number `b`. For example: `solve(15,12) = False` because `15` is not divisible by all the prime factors of `12` (which include`2`).

See test cases for more examples. 

Good luck!

If you like this Kata, please try:

[Sub-array division](https://www.codewars.com/kata/59eb64cba954273cd4000099)

[Divisor harmony](https://www.codewars.com/kata/59bf97cd4f98a8b1cd00007e)
"""

import math

def is_divisible_by_prime_factors(a: int, b: int) -> bool:
    c = math.gcd(a, b)
    while c > 1:
        b //= c
        c = math.gcd(a, b)
    return b == 1
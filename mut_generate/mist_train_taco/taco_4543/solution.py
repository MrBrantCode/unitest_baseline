"""
QUESTION:
A pair of numbers has a unique LCM but a single number can be the LCM of more than one possible
pairs. For example `12` is the LCM of `(1, 12), (2, 12), (3,4)` etc. For a given positive integer N, the number of different integer pairs with LCM is equal to N can be called the LCM cardinality of that number N. In this kata your job is to find out the LCM cardinality of a number.
"""

from itertools import combinations
from math import gcd

def calculate_lcm_cardinality(n):
    def divisors(n):
        d = {1, n}
        for k in range(2, int(n ** 0.5) + 1):
            if n % k == 0:
                d.add(k)
                d.add(n // k)
        return sorted(d)

    def lcm(a, b):
        return a * b // gcd(a, b)

    return 1 + sum((1 for (a, b) in combinations(divisors(n), 2) if lcm(a, b) == n))
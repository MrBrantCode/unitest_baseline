"""
QUESTION:
Factorize a given integer n.

Constraints

* 2 ≤ n ≤ 109

Input


n


An integer n is given in a line.

Output

Print the given integer n and :. Then, print prime factors in ascending order. If n is divisible by a prime factor several times, the prime factor should be printed according to the number of times. Print a space before each prime factor.

Examples

Input

12


Output

12: 2 2 3


Input

126


Output

126: 2 3 3 7
"""

import math

def factorize_integer(n):
    factors = []
    n1 = n
    p = 2
    
    while p <= math.sqrt(n):
        if n % p == 0:
            n //= p
            factors.append(str(p))
        else:
            p += 1
    
    if n != 1:
        factors.append(str(n))
    
    return f"{n1}: {' '.join(factors)}"
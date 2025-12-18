"""
QUESTION:
Write a function called `find_distinct_squarefree_sum` that calculates the sum of distinct squarefree numbers in the first 51 rows of Pascal's triangle. The function should not take any parameters. A number is considered squarefree if it is not divisible by the square of a prime number.
"""

import math

def is_squarefree(n):
    primes_square = [4, 9, 25, 49, 121, 169, 289, 361, 529, 841, 961, 1369, 1681, 1849, 2209]
    for p in primes_square:
        if n % p == 0:
            return False
    return True

def find_distinct_squarefree_sum():
    squarefree = set()
    for n in range(51):
        for k in range(n + 1):
            binomial = math.comb(n, k)
            if binomial not in squarefree and is_squarefree(binomial):
                squarefree.add(binomial)
    return sum(squarefree)
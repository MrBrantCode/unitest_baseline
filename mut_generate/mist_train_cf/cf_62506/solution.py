"""
QUESTION:
Write a function `deranged_probability` that takes no arguments and returns the probability of a derangement of 22 distinct prime numbers, approximated to 12 decimal places. The derangement is a permutation where none of the 22 prime numbers appear in their original positions. The function should use the formula `!n/n!` where `!n` is the number of derangements of a set of size `n` and `n!` is the number of permutations of a set of size `n`.
"""

from math import factorial

def derangement(n):
    der = [0,1]
    for i in range(2, n+1):
        der.append((i - 1) * (der[i - 1] + der[i - 2]))
    return der[n]

def deranged_probability(n):
    der = derangement(n)
    fact = factorial(n)
    prob = der/fact
    return round(prob, 12)
"""
QUESTION:
Goldbach's Conjecture: For any even number n greater than or equal to 4, there exists at least one pair of prime numbers p1 and p2 such that n = p1 + p2.

This conjecture has not been proved nor refused yet. No one is sure whether this conjecture actually holds. However, one can find such a pair of prime numbers, if any, for a given even number. The problem here is to write a program that reports the number of all the pairs of prime numbers satisfying the condition in the conjecture for a given even number.

A sequence of even numbers is given as input. Corresponding to each number, the program should output the number of pairs mentioned above. Notice that we are intereseted in the number of essentially different pairs and therefore you should not count (p1, p2) and (p2, p1) separately as two different pairs.



Input

An integer is given in each input line. You may assume that each integer is even, and is greater than or equal to 4 and less than 215. The end of the input is indicated by a number 0.

Output

Each output line should contain an integer number. No other characters should appear in the output.

Example

Input

6
10
12
0


Output

1
2
1
"""

import math

def primes(n):
    sieve = [1] * (n + 1)
    rt = int(math.sqrt(n))
    sieve[0] = sieve[1] = 0
    for p in range(2, rt + 1):
        if sieve[p] == 0:
            continue
        k = p * 2
        while k <= n:
            sieve[k] = 0
            k += p
    r = []
    for p in range(2, n + 1):
        if sieve[p] == 1:
            r.append(p)
    return r

def count_goldbach_pairs(n):
    if n < 4 or n % 2 != 0:
        raise ValueError("Input must be an even number greater than or equal to 4.")
    
    prime_list = primes(2 ** 15)
    c = 0
    for p in prime_list:
        if p <= n - p and n - p in prime_list:
            c += 1
    return c
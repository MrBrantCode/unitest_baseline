"""
QUESTION:
Xenny has 2 positive integers A and B. He wants to find the prime factorization of the integer A^B.

Input format:

Each line contains 2 space-separated integers A and B.

Output format:

Consider A^B to have N prime factors.
Print N lines.
For every prime factor, print the base and the exponent separated by a single space.
The prime factors must be sorted by base.

Constraints:

1 ≤ A ≤ 10^12

1 ≤ B ≤ 1000

SAMPLE INPUT
10 1

SAMPLE OUTPUT
2 1
5 1
"""

import math

# Precomputed prime list and skip list
primelist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
skiplist = [1, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 179, 191, 193, 197, 199]

def isprime(p):
    i = 0
    temp = math.sqrt(p)
    while primelist[i] <= temp:
        if p % primelist[i] == 0:
            return False
        i += 1
    return True

def prime_factorization_of_power(A, B):
    if A == 1:
        return [(1, 1)]
    
    sqrt_a = math.sqrt(A)
    list_limit = int(sqrt_a / 200)
    
    # Extend the prime list if necessary
    for i in range(1, list_limit):
        for j in range(0, 43):
            temp = 210 * i + skiplist[j]
            if isprime(temp):
                primelist.append(temp)
    
    prime_factors = []
    for z in primelist:
        count = 0
        while A % z == 0:
            A //= z
            count += 1
        if count > 0:
            prime_factors.append((z, count * B))
        if A <= 1:
            break
    
    if A > 1:
        prime_factors.append((A, B))
    
    return prime_factors
"""
QUESTION:
Given an `m x n` matrix `mat` where every row is sorted in strictly increasing order, find the smallest common prime element in all rows. If there is no common prime element, return `-1`. The function `smallestCommonElement(mat)` should return the result. 

The function must work under the following constraints: 
`m == mat.length`, `n == mat[i].length`, `1 <= m, n <= 500`, and `1 <= mat[i][j] <= 10^4`.
"""

import collections
def smallestCommonElement(mat):
    m, n = len(mat), len(mat[0])
    primes = [True] * 10001
    p = 2
    while (p * p <= 10000):
        if primes[p] == True:
            for i in range(p * p, 10001, p):
                primes[i] = False
        p += 1
    primes[0], primes[1] = False, False
    prime_list = [i for i in range(10001) if primes[i]]
    counter = collections.Counter()
    for row in mat:
        counter += collections.Counter(row)
    for p in prime_list:
        if counter[p] == m:
            return p
    return -1
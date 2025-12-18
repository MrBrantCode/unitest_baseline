"""
QUESTION:
A permutation p of size n is an array such that every integer from 1 to n occurs exactly once in this array.

Let's call a permutation an almost identity permutation iff there exist at least n - k indices i (1 ≤ i ≤ n) such that p_{i} = i.

Your task is to count the number of almost identity permutations for given numbers n and k.


-----Input-----

The first line contains two integers n and k (4 ≤ n ≤ 1000, 1 ≤ k ≤ 4).


-----Output-----

Print the number of almost identity permutations for given n and k.


-----Examples-----
Input
4 1

Output
1

Input
4 2

Output
7

Input
5 3

Output
31

Input
5 4

Output
76
"""

import math

def calculate_derangement(fac, n):
    ans = fac[n]
    for i in range(1, n + 1):
        if i % 2 == 1:
            ans -= fac[n] // fac[i]
        else:
            ans += fac[n] // fac[i]
    return ans

def count_almost_identity_permutations(n, k):
    fac = [1]
    for i in range(1, n + 1):
        fac.append(fac[i - 1] * i)
    
    ans = 0
    for i in range(0, k + 1):
        choose = fac[n]
        choose //= fac[i]
        choose //= fac[n - i]
        ans += choose * calculate_derangement(fac, i)
    
    return ans
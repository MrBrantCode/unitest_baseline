"""
QUESTION:
Squirrel Liss is interested in sequences. She also has preferences of integers. She thinks n integers a1, a2, ..., an are good.

Now she is interested in good sequences. A sequence x1, x2, ..., xk is called good if it satisfies the following three conditions:

  * The sequence is strictly increasing, i.e. xi < xi + 1 for each i (1 ≤ i ≤ k - 1). 
  * No two adjacent elements are coprime, i.e. gcd(xi, xi + 1) > 1 for each i (1 ≤ i ≤ k - 1) (where gcd(p, q) denotes the greatest common divisor of the integers p and q). 
  * All elements of the sequence are good integers. 



Find the length of the longest good sequence.

Input

The input consists of two lines. The first line contains a single integer n (1 ≤ n ≤ 105) — the number of good integers. The second line contains a single-space separated list of good integers a1, a2, ..., an in strictly increasing order (1 ≤ ai ≤ 105; ai < ai + 1).

Output

Print a single integer — the length of the longest good sequence.

Examples

Input

5
2 3 4 6 9


Output

4


Input

9
1 2 3 5 6 7 8 9 10


Output

4

Note

In the first example, the following sequences are examples of good sequences: [2; 4; 6; 9], [2; 4; 6], [3; 9], [6]. The length of the longest good sequence is 4.
"""

from collections import Counter

def seieve_prime_factorisation(n):
    (p, i) = ([1] * (n + 1), 2)
    while i * i <= n:
        if p[i] == 1:
            for j in range(i * i, n + 1, i):
                p[j] = i
        i += 1
    return p

def prime_factorisation_by_seive(p, x):
    c = Counter()
    while p[x] != 1:
        c[p[x]] += 1
        x = x // p[x]
    c[x] += 1
    return c

def find_longest_good_sequence_length(good_integers):
    n = len(good_integers)
    p = seieve_prime_factorisation(max(good_integers))
    dp = [1] * n
    b = Counter()
    for i in range(n - 1, -1, -1):
        z = prime_factorisation_by_seive(p, good_integers[i])
        ma = 0
        for j in z:
            ma = max(ma, b[j])
        dp[i] += ma
        for j in z:
            b[j] = max(b[j], dp[i])
    return max(dp)
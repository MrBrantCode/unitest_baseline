"""
QUESTION:
This time your assignment is really simple.

Calculate GCD(1, 1) * GCD(1, 2) * ... * GCD(1, M) * GCD(2, 1) * GCD(2, 2) * ... * GCD(2, M) * ... * GCD(N, 1) * GCD(N, 2) * ... * GCD(N, M).

where GCD is defined as the Greatest Common Divisor. 

Input Format

The first and only line contains two space separated integers N and M.

Output Format

Output the required product modulo 10^{9}+7.

Constraints

1 <= N, M <= 1.5 * 10^{7}

Sample input:

4 4

Sample output:

96

Explanation

For the above testcase, N = 4, M = 4. So, 

GCD(1, 1) * GCD(1, 2) * ...... * GCD(4, 4) = 1 * 1 * 1 * 1 * 1 * 2 * 1 * 2 * 1 * 1 * 3 * 1 * 1 * 2 * 1 * 4 = 96.
"""

import math

MOD = 1000000007

def rwh_primes2(n):
    if n < 3:
        return []
    elif n == 3:
        return [2]
    elif n < 6:
        return [2, 3]
    correction = n % 6 > 1
    n = {0: n, 1: n - 1, 2: n + 4, 3: n + 3, 4: n + 2, 5: n + 1}[n % 6]
    sieve = [True] * (n // 3)
    sieve[0] = False
    for i in range(int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k // 3::2 * k] = [False] * ((n // 6 - k * k // 6 - 1) // k + 1)
            sieve[(k * k + 4 * k - 2 * k * (i & 1)) // 3::2 * k] = [False] * ((n // 6 - (k * k + 4 * k - 2 * k * (i & 1)) // 6 - 1) // k + 1)
    return [2, 3] + [3 * i + 1 | 1 for i in range(1, n // 3 - correction) if sieve[i]]

def calculate_gcd_product(N, M):
    (N, M) = (min(N, M), max(N, M))
    primes = rwh_primes2(M + 1)
    product = 1
    for p in primes:
        n = 0
        k = p
        while k <= N:
            n += N // k * (M // k)
            k *= p
        product *= pow(p, n, MOD)
        product %= MOD
    return product
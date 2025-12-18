"""
QUESTION:
Create a function `find_primes(m, n)` that finds all prime numbers within a given range `[m, n]` where `1 ≤ m ≤ n ≤ 10^9` and returns them as a list. The function should have a time complexity of O(n log log n). If `m` is 1, it should be treated as if it were 2. You cannot use any external libraries or built-in functions that directly solve this problem.
"""

def find_primes(m, n):
    if m == 1:
        m = 2

    is_prime = [True] * (n + 1)
    primes = []

    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    for i in range(m, n + 1):
        if is_prime[i]:
            primes.append(i)

    return primes
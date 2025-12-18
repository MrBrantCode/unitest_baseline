"""
QUESTION:
Write a function `lexicalOrder` that takes an integer `n` as input and returns a tuple of two values. The first value is a list of integers from 1 to `n` in lexicographical order, and the second value is the sum of all prime numbers in the list. The input `n` is guaranteed to be in the range `[1, 5*10^4]`.
"""

def lexicalOrder(n: int) -> list:
    def sieve(n: int) -> list:
        primes = [True] * (n+1)
        p = 2
        while p*p <= n:
            if primes[p] == True:
                for i in range(p*p, n+1, p):
                    primes[i] = False
            p += 1
        return primes

    def dfs(n, curr, primes, res, sum_primes):
        if curr > n:
            return
        res.append(curr)
        sum_primes[0] += curr if ((curr != 0 and curr != 1) and primes[curr]) else 0
        for i in range(10):
            if 10 * curr + i > n:
                return
            dfs(n, 10 * curr + i, primes, res, sum_primes)
        
    res = []
    sum_primes = [0]
    primes = sieve(n)
    for i in range(1, 10):
        dfs(n, i, primes, res, sum_primes)
    return (res, sum_primes[0])
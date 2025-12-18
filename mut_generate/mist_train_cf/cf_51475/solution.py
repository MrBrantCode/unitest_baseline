"""
QUESTION:
Define the function M(p, q, N) as the largest positive integer ≤ N that is exclusively divisible by distinct primes p and q. If no such integer exists, M(p, q, N) = 0. Define S(N) as the sum of all unique M(p, q, N). Write a function find_S(N) to calculate S(N) for a given positive integer N. Note that p and q should be distinct prime numbers and N should be a positive integer.
"""

def find_S(n):
    def find_PRIMES(n):
        sieve = [True] * n
        for i in range(3,int(n**0.5)+1,2):
            if sieve[i]:
                sieve[i*i::2*i] = [False] * ((n-i*i-1)//(2*i)+1)
        return [2] + [i for i in range(3,n,2) if sieve[i]]

    def find_M_value(p, q, n):
        if p == 2:
            pp = 1
            while (pp * 2 * q <= n):
                pp *= 2
            return pp * q
        else:
            pp = p
            qq = q
            while (pp * q <= n):
                pp *= p
            while (pp * qq <= n):
                qq *= q
            return pp * qq

    primes = find_PRIMES(int(n**0.5) + 1)
    prime_length = len(primes)
    primes_set = set(primes)
    S = 0

    for i in range(prime_length):
        p = primes[i]
        for j in range(i+1, prime_length):
            q = primes[j]
            S += find_M_value(p, q, n)
            if (p * q > n):
                break
            r = p * q
            while (r * p <= n):
                r *= p
            while (r * q <= n):
                r *= q
            while (r not in primes_set):
                r += n
                if (r > n):
                    break
            if (r in primes_set):
                S -= r
    return S
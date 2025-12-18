"""
QUESTION:
Determine the function G(N) which is the sum of g(p) for all prime numbers p less than N. Here, g(p) is defined as f(p) mod p and f(p) is equivalent to 2^(2^p % p) mod 2^p. Write the function G(N) that takes an integer N as input and returns the sum. 

Restrictions: N is a large number, direct computation would be very slow.
"""

def G(N):
    is_prime = [False, False] + [True] * (N - 1)
    for x in range(2, int(N ** 0.5) + 1):
        if is_prime[x]:
            is_prime[x * x:N:x] = [False] * len(is_prime[x * x:N:x])
    return sum(pow(2, 2 % p, p) for p in range(2, N+1) if is_prime[p])
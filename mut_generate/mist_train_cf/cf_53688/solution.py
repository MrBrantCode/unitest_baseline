"""
QUESTION:
Implement the function `D(a, b, k)` that calculates the sum of `d(p, p-1, k) mod p` for all primes `p` in the range `a ≤ p < a + b`. The function `d(p, n, k)` represents the `k`-th generation of multiplicative inverses under modulo `p`, defined as `d(p, n, 0) = n^(-1) mod p` and `d(p, n, k) = ∑[d(p, i, k-1) for i from 1 to n]`.
"""

def D(a, b, k):
    def is_prime(n):
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def mod_inverse(a, m):
        """Compute the modular multiplicative inverse."""
        def extended_gcd(a, b):
            if a == 0:
                return b, 0, 1
            else:
                gcd, x, y = extended_gcd(b % a, a)
                return gcd, y - (b // a) * x, x

        gcd, x, _ = extended_gcd(a, m)
        if gcd != 1:
            return None
        else:
            return x % m

    def d(p, n, k):
        """Compute the k-th generation of multiplicative inverses under modulo p."""
        if k == 0:
            return mod_inverse(n, p)
        else:
            result = 0
            for i in range(1, n + 1):
                result += d(p, i, k - 1)
            return result % p

    total = 0
    for p in range(a, a + b):
        if is_prime(p):
            total += d(p, p - 1, k)
            total %= p
    return total
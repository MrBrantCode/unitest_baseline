"""
QUESTION:
Implement a function `B(x, y, n)` to calculate the summation of `(a_n mod p)` for each prime number `p` within the range `x ≤ p ≤ x+y`, where `a_n` is defined by the recursive sequence `a_1 = 1` and `a_{n+1} = 6a_n^2 + 10a_n + 3` for `n ≥ 1`, with all calculations performed modulo `1,000,000,007`.
"""

def B(x, y, n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    mod = 1000000007
    a_n = 1
    total_sum = 0

    for _ in range(n - 1):
        a_n = (6 * a_n**2 + 10 * a_n + 3) % mod

    for p in range(x, x + y + 1):
        if is_prime(p):
            total_sum += a_n % p

    return total_sum
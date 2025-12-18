"""
QUESTION:
Create a function called `find_primes(m, n)` to find all prime numbers within the range [m, n], where 1 ≤ m ≤ n ≤ 10^9. The function should handle the case where m equals 1 and must have a time complexity of O(n log log n) without using any external libraries or built-in functions that directly solve this problem.
"""

def find_primes(m, n):
    if m == 1:
        m = 2

    # Create a boolean array "is_prime[0..n]" and initialize all entries as true
    is_prime = [True] * (n + 1)

    p = 2
    while p * p <= n:
        # If is_prime[p] is not changed, then it is a prime
        if is_prime[p]:
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    # Add primes within the given range to the primes list
    return [i for i in range(m, n + 1) if is_prime[i]]
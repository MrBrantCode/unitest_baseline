"""
QUESTION:
Write a function `generate_primes(n)` that takes an integer `n` as input and returns a list of all prime numbers from 0 to `n` without using any built-in functions or libraries for prime number generation. The function should have a time complexity of O(n√n) or better.
"""

def generate_primes(n):
    # Create a boolean array "is_prime[0..n]" and initialize all entries it as true.
    # A value in is_prime[i] will finally be false if i is Not a prime, else true.
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    # Iterate through all numbers up to square root of n
    for i in range(2, int(n**0.5) + 1):
        # If is_prime[i] is not changed, then it is a prime
        if is_prime[i]:
            # Update all multiples of i to be not prime
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    # Generate list of primes
    primes = []
    for i in range(2, n+1):
        if is_prime[i]:
            primes.append(i)

    return primes
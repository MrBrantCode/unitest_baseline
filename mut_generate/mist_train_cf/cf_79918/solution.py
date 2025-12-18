"""
QUESTION:
Write a function named `check_primality_and_parity` that takes an integer `n` as input. The function should return three values: a string describing whether `n` is prime or composite, a string describing whether `n` is even or odd, and a list of prime factors of `n` if it is composite. The function should assume that the input `n` is a positive integer.
"""

def check_primality_and_parity(n):
    # check if n is even or odd
    parity = "Even" if n % 2 == 0 else "Odd"
    # check if n is prime or composite
    def prime_factors(n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors

    # starting obvious check that n is not less than 2
    if n < 2:
        return "Number must be greater than 1", parity, []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "Composite", parity, prime_factors(n)
    return "Prime", parity, []
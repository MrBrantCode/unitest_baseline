"""
QUESTION:
Create a function `prime_factorization(n)` that takes an integer `n` greater than 1 as input and returns a dictionary with prime factors as keys and their respective powers as values. The function should also print the prime factorization of `n`. The input `n` should be validated to ensure it's a positive integer greater than 1.
"""

def prime_factorization(n):
    # Check if input is a positive integer
    if not isinstance(n, int) or n < 2:
        print('Input must be a positive integer greater than 1.')
        return None

    prime_factors = {}  # Dictionary to hold prime factors

    # Divide n by 2 until n is odd
    while n % 2 == 0:
        prime_factors[2] = prime_factors.get(2, 0) + 1  # If 2 is already a key, increment its value. If not, assign it a value of 1.
        n = n // 2

    # n must be odd at this point, so we can skip one element (we increment i by 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            prime_factors[i] = prime_factors.get(i, 0) + 1
            n = n // i

    # This condition is to handle the case when n is a prime number greater than 2
    if n > 2:
        prime_factors[n] = prime_factors.get(n, 0) + 1

    # Print out prime factorization
    factors = [f'{key}^{value}' for key, value in prime_factors.items()]
    print(' * '.join(factors))

    # Return dictionary of prime factors
    return prime_factors
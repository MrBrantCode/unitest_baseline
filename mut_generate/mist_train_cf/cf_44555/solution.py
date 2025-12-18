"""
QUESTION:
Create a function named `prime_factors` that takes a single positive integer `n` as input and returns a dictionary containing the prime factors of `n` as keys and their corresponding frequencies as values. The function should handle non-integer and negative inputs by returning an error message.
"""

def prime_factors(n):
    # Handle non-integers and negative numbers
    if not isinstance(n, int) or n <= 0:
        return "Error: Input should be a positive integer."

    i = 2
    factors = {}
    while i*i <= n:
        if n % i:
            i += 1
        else:
            # Dividing by prime factor
            n //= i
            # Recording or incrementing prime factor count
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
    # If no more divisors are possible (prime number), record the number itself
    if n > 1:
        if n in factors:
            factors[n] += 1
        else:
            factors[n] = 1
    return factors
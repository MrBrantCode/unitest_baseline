"""
QUESTION:
Create a Python class with a method named `calculate_primes` that takes an integer `n` as input and returns a list of prime numbers up to `n`. The input value `n` should be greater than or equal to 2. The method should handle edge cases such as negative input values and non-integer inputs, and should be efficient and able to handle large input values without using any built-in functions or libraries for prime number generation or mathematical operations.
"""

def calculate_primes(n):
    # Handle edge cases
    if not isinstance(n, int) or n < 2:
        return []

    primes = []
    for num in range(2, n+1):
        is_prime = True
        for divisor in range(2, int(num**0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

    return primes
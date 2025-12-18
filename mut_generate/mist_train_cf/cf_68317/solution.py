"""
QUESTION:
Write a recursive function named `print_primes` that takes an integer `n` as input, prints all prime numbers up to `n` (inclusive) each on a separate line, and uses a helper function `is_prime` to check if a number is prime. The function should handle numbers up to 300.
"""

def print_primes(n, i=2):
    # Base case
    if i > n:
        return

    # If current number is prime, print it
    if is_prime(i):
        print(i)
    
    # Check next number
    return print_primes(n, i + 1)


def is_prime(n, i=2):
    # Base cases
    if n <= 2:
        return False if (n < 2) else True
    if n % i == 0:
        return False
    if i * i > n:
        return True
 
    # Check for next divisor
    return is_prime(n, i + 1)
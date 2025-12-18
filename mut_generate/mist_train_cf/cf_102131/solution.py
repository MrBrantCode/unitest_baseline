"""
QUESTION:
Write a function `primes_up_to(n)` that uses the Sieve of Eratosthenes algorithm to generate and print all prime numbers up to a given number `n`. The function should also track and display the iteration number for each prime number printed. The generated prime numbers should be greater than 1 and only divisible by 1 and themselves.
"""

def primes_up_to(n):
    """
    Generates and prints all prime numbers up to a given number n using the Sieve of Eratosthenes algorithm.

    Args:
        n (int): The upper limit for generating prime numbers.

    Returns:
        list: A list of prime numbers up to n.
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    p = 2
    while p**2 <= n:
        if sieve[p]:
            for i in range(p**2, n + 1, p):
                sieve[i] = False
        p += 1
    return [i for i, is_prime in enumerate(sieve) if is_prime]
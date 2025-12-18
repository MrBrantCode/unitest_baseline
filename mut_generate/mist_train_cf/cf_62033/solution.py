"""
QUESTION:
Write two functions, `is_prime` and `primes_up_to`, where `is_prime` checks whether a given number is prime using a list of known primes up to the square root of that number, and `primes_up_to` generates all prime numbers up to a given number. The function `is_prime` should take two parameters, `n` and `known_primes`, and return `True` if `n` is prime and `False` otherwise. The function `primes_up_to` should take one parameter `n` and return a list of all prime numbers up to `n`. The function `primes_up_to` should use the `is_prime` function to check if a number is prime.
"""

def is_prime(n, known_primes):
    """
    Checks whether a given number is prime using a list of known primes up to the square root of that number.

    Args:
    n (int): The number to check for primality.
    known_primes (list): A list of known prime numbers.

    Returns:
    bool: True if n is prime, False otherwise.
    """
    for prime in known_primes:
        if prime*prime > n:
            break
        if n % prime == 0:  # 是合數
            return False
    return True

def primes_up_to(n):
    """
    Generates all prime numbers up to a given number.

    Args:
    n (int): The upper limit for generating prime numbers.

    Returns:
    list: A list of prime numbers up to n.
    """
    known_primes = [2]
    i = 3
    while i <= n:
        if is_prime(i, known_primes):
            known_primes.append(i)
        #_check Only odd numbers
        i += 2
    return known_primes
"""
QUESTION:
Write a function `find_prime_numbers(n)` that finds all prime numbers between 1 and a given positive integer `n`, without using any built-in libraries or functions for prime number calculation or checking. The function should return a list of prime numbers and have a time complexity of O(n*sqrt(n)).
"""

def find_prime_numbers(n):
    """
    Finds all prime numbers between 1 and a given positive integer n.

    Args:
    n (int): A positive integer.

    Returns:
    list: A list of prime numbers between 1 and n.

    """
    primes = []
    for possiblePrime in range(2, n + 1):
        # Assume number is prime until shown it is not. 
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    return primes
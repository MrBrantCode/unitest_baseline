"""
QUESTION:
Write a function called `find_primes` that finds all prime numbers below a given number `n`. The function should return a tuple containing the count of prime numbers found and a list of the prime numbers.
"""

def find_primes(n):
    """
    Finds all prime numbers below a given number n.
    
    Args:
        n (int): The upper limit below which to find prime numbers.
    
    Returns:
        tuple: A tuple containing the count of prime numbers found and a list of the prime numbers.
    """
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_numbers = [num for num in range(2, n) if is_prime(num)]
    count = len(prime_numbers)
    return (count, prime_numbers)
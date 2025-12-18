"""
QUESTION:
Create a function named `get_prime_numbers` that takes a list of integers as input and returns a new list containing only the prime numbers from the original list. You cannot use built-in functions or libraries for prime number calculation.
"""

def get_prime_numbers(numbers):
    """
    Return a new list with all the prime numbers from the original list.
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    return primes
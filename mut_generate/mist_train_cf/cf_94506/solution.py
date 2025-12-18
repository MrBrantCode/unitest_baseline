"""
QUESTION:
Implement a function `get_unique_primes` that takes a list of integers as input and returns a set containing the unique prime numbers from the list.
"""

def get_unique_primes(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    unique_primes = set()
    for num in numbers:
        if is_prime(num):
            unique_primes.add(num)
    
    return unique_primes
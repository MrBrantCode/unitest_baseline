"""
QUESTION:
Write a function named `find_largest_prime` that takes a list of integers as input and returns the largest prime number in the list. If the list does not contain any prime numbers, the function should return `None`.
"""

def find_largest_prime(numbers):
    primes = []
    
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    
    return max(primes) if len(primes) > 0 else None
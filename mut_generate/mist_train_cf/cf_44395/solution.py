"""
QUESTION:
Write a recursive function to find and display the prime numbers in the sequence from 1 to 200, along with their total count and sum. The function should handle large integers efficiently.
"""

def display_primes(n):
    def is_prime(num): 
        if num <= 1: 
            return False
        if num == 2: 
            return True
        if num % 2 == 0: 
            return False
        i = 3
        while i * i <= num: 
            if num % i == 0: 
                return False
            i += 2
        return True

    primes = [x for x in range(1, n+1) if is_prime(x)]
    return primes, len(primes), sum(primes)
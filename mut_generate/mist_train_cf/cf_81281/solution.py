"""
QUESTION:
Implement a function `generate_primes(n)` to generate a list of all prime numbers in the range from 0 to `n`. The function should not use any built-in or library functions for prime number generation directly. The function should be optimized with a time complexity better than O(n^2).
"""

def generate_primes(n):
    primes = list()
    for num in range(2, n + 1):
        is_prime = True
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                is_prime = False
                break
                
        if is_prime:
            primes.append(num)
            
    return primes
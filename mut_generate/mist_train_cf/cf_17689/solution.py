"""
QUESTION:
Create a function named `generate_prime_numbers` that takes an integer `n` greater than 2 as input, and returns a list of consecutive prime numbers starting from 2 up to `n`. The function should have a time complexity of O(n^2) or less and use a memory-efficient approach to store the prime numbers.
"""

def generate_prime_numbers(n):
    primes = [2]
    current_number = 3

    while current_number <= n:
        is_prime = True
        for prime in primes:
            if prime * prime > current_number:
                break
            if current_number % prime == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(current_number)

        current_number += 2

    return primes
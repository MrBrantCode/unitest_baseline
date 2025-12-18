"""
QUESTION:
Create a function `replace_primes_with_cubes` that takes a list of consecutive integers as input. Identify the prime numbers in the list, replace each prime number with its cube, and return the modified list. The function should work with any input list of consecutive integers.
"""

def replace_primes_with_cubes(sequence):
    def check_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    for i in range(len(sequence)):
        if check_prime(sequence[i]):
            sequence[i] = sequence[i]**3
    return sequence
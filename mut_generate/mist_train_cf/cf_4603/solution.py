"""
QUESTION:
Construct a function named `prime_list_repeated` that generates a list of prime numbers between two given integers `m` and `n` (inclusive), where each prime number is repeated twice and the list is sorted in ascending order. The input values `m` and `n` are both positive integers greater than 1.
"""

def prime_list_repeated(m, n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = [i for i in range(m, n + 1) if is_prime(i)]
    return sorted(primes * 2)
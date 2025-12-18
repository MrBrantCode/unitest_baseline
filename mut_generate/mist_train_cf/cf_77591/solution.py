"""
QUESTION:
Write a function `primes_cubed(num)` that returns a list of the cubed values of all prime numbers less than or equal to the provided number `num`.
"""

def primes_cubed(num):
    prime_cubed_list = []

    for possible_prime in range(2, num + 1):
        is_prime = True
        for num in range(2, possible_prime):
            if possible_prime % num == 0:
                is_prime = False
        if is_prime:
            prime_cubed_list.append(possible_prime ** 3)

    return prime_cubed_list
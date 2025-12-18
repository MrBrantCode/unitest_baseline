"""
QUESTION:
Create a Python function named `last_n_unique_primes` that takes a list of positive integers and an integer `n` as input. The function should return the last `n` unique prime numbers from the list, excluding duplicates. If the list contains fewer than `n` unique prime numbers, the function should return all the unique prime numbers in the list.
"""

def last_n_unique_primes(numbers, n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    unique_primes = set()
    for num in numbers:
        if is_prime(num):
            unique_primes.add(num)
    return list(unique_primes)[-n:]
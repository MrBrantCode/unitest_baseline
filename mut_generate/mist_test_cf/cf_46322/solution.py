"""
QUESTION:
Write a function called `count_up_to` that accepts a non-negative integer `n` and returns a list of prime numbers less than `n`. The function should also include a mechanism to validate the accuracy of the implemented algorithm and measure its efficiency. The input `n` should be a non-negative integer, and the function should return a list of integers.
"""

import time

def count_up_to(n):
    """Return all primes less than n and measure efficiency."""
    if n < 2: return []

    start_time = time.time()
    primes = [2]
    i = 3
    while i < n:
        if all(i % p != 0 for p in primes):
            primes.append(i)
        i += 2

    print(f"Time taken: {time.time() - start_time} seconds.")

    # validate the correctness
    def is_prime(num):
        if num < 2: return False
        if num == 2 or num == 3: return True
        if num % 2 == 0 or num % 3 == 0: return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0: return False
            i += 6
        return True

    if not all(is_prime(p) for p in primes):
        print("The algorithm is not correct.")
    else:
        print("The algorithm is correct.")

    return primes
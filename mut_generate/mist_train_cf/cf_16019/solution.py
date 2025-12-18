"""
QUESTION:
Write a function called `print_prime_numbers` that takes two integers `start` and `end` as input, representing a range, and returns a list of all prime numbers in the range from `start` to `end` (inclusive) with a time complexity of O(n log(log n)). The function should not use any built-in functions or libraries for checking prime numbers.
"""

def print_prime_numbers(start, end):
    primes = []
    is_prime = [True] * (end + 1)
    is_prime[0] = is_prime[1] = False

    p = 2

    while p * p <= end:
        if is_prime[p]:
            for i in range(p * p, end + 1, p):
                is_prime[i] = False

        p += 1

    for p in range(start, end + 1):
        if is_prime[p]:
            primes.append(p)

    return primes
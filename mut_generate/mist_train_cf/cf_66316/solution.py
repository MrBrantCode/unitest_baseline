"""
QUESTION:
Create a function named `prime_sum_and_largest_factor(n)` that takes an integer `n` as input and performs the following operations:

- Generate a list of prime numbers from `n` down to 1.
- Calculate the sum of these prime numbers.
- Find the largest prime factor of `n`.

The function should then return or print the list of prime numbers, the sum of prime numbers, and the largest prime factor of `n`. The prime numbers should be listed in reverse order, from `n` down to 1.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_sum_and_largest_factor(n):
    primes = [i for i in range(n, 0, -1) if is_prime(i)]
    primes_sum = sum(primes)
    largest_prime_factor = next((x for x in primes if n % x == 0), None)

    print("Prime numbers:", primes)
    print("Sum of prime numbers:", primes_sum)
    print("Largest prime factor:", largest_prime_factor)
"""
QUESTION:
Create a function named `separate_primes_and_composites` that takes a list of integers as input and returns two lists of integers. The first list should contain the prime numbers from the input list in reverse order, and the second list should contain the composite numbers from the input list in reverse order. The function should not take any other arguments besides the input list.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def separate_primes_and_composites(numbers):
    prime_numbers = [i for i in numbers if is_prime(i)]
    composite_numbers = [i for i in numbers if not is_prime(i)]
    return prime_numbers[::-1], composite_numbers[::-1]
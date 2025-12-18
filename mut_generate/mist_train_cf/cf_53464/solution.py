"""
QUESTION:
Write a function `compute` that takes a list of integers as input, identifies the smallest prime number in the list, and returns the product of its digits. If no prime numbers are found, return 0. Assume that the input list is non-empty.
"""

def compute(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_numbers = [i for i in lst if is_prime(i)]
    if not prime_numbers:
        return 0
    smallest_prime = min(prime_numbers)
    product = 1
    while smallest_prime:
        digit = smallest_prime % 10
        product *= digit
        smallest_prime //= 10
    return product
"""
QUESTION:
Design a function `sum_of_primes(numbers)` that takes a list of integers `numbers` as input and returns the sum of all prime numbers in the list.
"""

def sum_of_primes(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_sum = 0
    for num in numbers:
        if is_prime(num):
            prime_sum += num
    return prime_sum
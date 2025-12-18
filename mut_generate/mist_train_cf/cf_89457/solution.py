"""
QUESTION:
Create a function `sum_of_primes` that takes in a list of integers and returns the sum of all the prime numbers in the list, excluding any numbers that are divisible by 5. If there are no prime numbers that are not divisible by 5, the function should return -1. The input list can contain negative numbers.
"""

def sum_of_primes(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_sum = 0
    for num in numbers:
        if is_prime(num) and num % 5 != 0:
            prime_sum += num

    return -1 if prime_sum == 0 else prime_sum
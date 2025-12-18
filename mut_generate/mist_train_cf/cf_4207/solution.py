"""
QUESTION:
Create a function called `sum_of_primes` that takes a list of integers as input and returns the sum of all prime numbers in the list. Implement the prime number checking logic within the function without using any built-in functions or libraries.
"""

def sum_of_primes(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_sum = 0
    for num in numbers:
        if is_prime(num):
            prime_sum += num
    return prime_sum
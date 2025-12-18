"""
QUESTION:
Write a function named `find_prime_numbers` that takes an integer `n` as input and returns a list of prime numbers less than `n` whose sum of digits is also a prime number. The function should use helper functions to check if a number is prime and calculate the sum of its digits.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def digit_sum(n):
    return sum(int(digit) for digit in str(n))

def find_prime_numbers(n):
    primes = []
    for num in range(2, n):
        if is_prime(num):
            num_sum = digit_sum(num)
            if is_prime(num_sum):
                primes.append(num)
    return primes
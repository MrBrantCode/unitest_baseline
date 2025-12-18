"""
QUESTION:
Write a function `find_prime_numbers` that takes a given integer `n` as input and returns a list of all prime numbers less than `n` where the sum of the digits of each prime number is also a prime number. The function should only consider integers from 2 to `n-1`.
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
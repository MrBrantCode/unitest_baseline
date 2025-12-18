"""
QUESTION:
Write a function `is_prime(num)` to check if a given number is prime or not, and a function `get_primes(start, end)` to return a list of all prime numbers within a given range. The function `is_prime(num)` should return True if the number is prime and False otherwise. The function `get_primes(start, end)` should return a list of prime numbers in the range from `start` to `end` (inclusive). Assume that the input numbers are positive integers.
"""

def is_prime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return False
        return True
    else:
        return False

def get_primes(start, end):
    prime_numbers = []
    for num in range(start, end+1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers
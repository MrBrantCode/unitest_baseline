"""
QUESTION:
Create a function named `is_prime` to check if a given number is prime. Additionally, create another function named `get_primes` that takes a range of numbers as input and returns a list of all prime numbers within that range. The `is_prime` function should return a boolean value indicating whether the input number is prime or not. The `get_primes` function should take two parameters, start and end, and return a list of prime numbers within the given range (inclusive).
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
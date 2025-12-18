"""
QUESTION:
Create a function `generate_prime_numbers()` that returns a list of prime numbers between 1000 and 2000 (inclusive) where the sum of the digits of each prime number is also a prime number.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def generate_prime_numbers():
    prime_numbers = []
    for num in range(1000, 2001):
        if is_prime(num) and is_prime(sum_of_digits(num)):
            prime_numbers.append(num)
    return prime_numbers
"""
QUESTION:
Write a function `generate_prime_list()` that generates a list of prime numbers between 1000 and 2000, where the sum of the digits of each prime number is a multiple of 5.
"""

def is_prime(n):
    """
    Checks if a number is prime.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime_list():
    """
    Generates a list of prime numbers between 1000 and 2000, where the sum of the digits is a multiple of 5.
    """
    prime_list = []
    for num in range(1000, 2001):
        digit_sum = sum(map(int, str(num)))  # Sum of digits
        if is_prime(num) and digit_sum % 5 == 0:
            prime_list.append(num)
    return prime_list
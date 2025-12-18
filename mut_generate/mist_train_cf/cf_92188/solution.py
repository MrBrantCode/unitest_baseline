"""
QUESTION:
Create a function `is_prime` to check if a number is prime and use it to generate a list of prime numbers from 1 to a given number, in this case, 100. The function should return False for numbers less than or equal to 1 and check divisibility up to the square root of the number.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
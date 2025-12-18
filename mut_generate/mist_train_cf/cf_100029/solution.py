"""
QUESTION:
Design a function named `is_prime` to check whether a given number is prime, and use it to generate the first 10 prime numbers between 1000 and 2000. Then, calculate the sum of the digits of these prime numbers. The `is_prime` function should take one integer as input and return a boolean value. The prime numbers and their sum of digits should be calculated and returned.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
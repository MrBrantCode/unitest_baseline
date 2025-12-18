"""
QUESTION:
Write a function to compute the product of all prime numbers from 1 to 500 using a while loop. The function should include a helper function `is_prime(n)` to check if a number `n` is prime or not.
"""

def is_prime(n):
    """
    Check if a number is prime.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def compute_prime_product():
    """
    Compute the product of all prime numbers from 1 to 500.
    """
    product = 1
    num = 2
    while num <= 500:
        if is_prime(num):
            product *= num
        num += 1
    return product
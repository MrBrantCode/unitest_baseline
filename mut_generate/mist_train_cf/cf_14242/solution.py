"""
QUESTION:
Write a function `product_of_primes` that takes a list of positive integers and returns an integer which is the product of all the prime numbers in the list. The function should use a helper function `is_prime` to check if a number is prime.
"""

def product_of_primes(numbers):
    product = 1
    for number in numbers:
        if is_prime(number):
            product *= number
    return product

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
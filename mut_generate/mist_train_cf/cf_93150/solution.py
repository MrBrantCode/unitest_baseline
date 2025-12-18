"""
QUESTION:
Write a function named `product_of_primes` that takes a list of positive integers as input and returns the product of all prime numbers in the list. The function should return an integer.
"""

def product_of_primes(numbers):
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True

    product = 1
    for number in numbers:
        if is_prime(number):
            product *= number
    return product
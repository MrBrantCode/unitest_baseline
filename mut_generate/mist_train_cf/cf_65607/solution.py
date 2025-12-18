"""
QUESTION:
Write a function named `multiply_prime_numbers` that returns the product of the first 10 prime numbers in the series of natural integers. The function should implement a method to check if a number is prime and then multiply the first 10 prime numbers.
"""

def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

def multiply_prime_numbers():
    count, num, prod = 0, 2, 1
    while count < 10:
        if is_prime(num):
            prod *= num
            count += 1
        num += 1
    return prod
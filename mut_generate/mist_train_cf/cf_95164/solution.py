"""
QUESTION:
Write a function named `square_of_prime_sum` that calculates the square of the sum of the first 1000 prime numbers greater than 100.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def square_of_prime_sum():
    count = 0
    num = 101
    prime_sum = 0
    while count < 1000:
        if is_prime(num):
            prime_sum += num
            count += 1
        num += 1
    return prime_sum**2
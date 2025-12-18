"""
QUESTION:
Write a function named `prime_numbers_in_range` that takes two integers `start` and `end` as input and returns a tuple. The tuple should contain a list of all prime numbers between `start` and `end` (inclusive), the product of all these prime numbers, and the sum of the digits of these prime numbers. The function should not take any other input and should not print any output. The prime numbers should be found using a helper function `is_prime(n)` that checks if a number `n` is prime.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers_in_range(start, end):
    prime_numbers = [num for num in range(start, end + 1) if is_prime(num)]
    product = 1
    for prime in prime_numbers:
        product *= prime
    sum_of_digits = sum(sum(int(digit) for digit in str(prime)) for prime in prime_numbers)
    return (prime_numbers, product, sum_of_digits)
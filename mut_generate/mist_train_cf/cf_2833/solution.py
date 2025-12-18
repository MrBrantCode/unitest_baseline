"""
QUESTION:
Create a function `prime_numbers(limit)` that finds all prime numbers below a given limit, filters them based on the following conditions, and returns the filtered list of prime numbers. The conditions are: the sum of the digits of each prime number is a prime number itself, the product of all prime numbers in the list is a prime number itself, the average of the prime numbers in the list is a prime number itself, and the length of the list of prime numbers is a prime number itself.
"""

import math

def prime_numbers(limit):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def digit_sum(n):
        return sum(int(digit) for digit in str(n))

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result

    def average(lst):
        return sum(lst) / len(lst)

    primes = []
    for num in range(2, limit):
        if is_prime(num):
            digit_sum_prime = is_prime(digit_sum(num))
            product_prime = is_prime(product(primes + [num]))
            average_prime = is_prime(average(primes + [num]))
            length_prime = is_prime(len(primes + [num]))
            if digit_sum_prime and product_prime and average_prime and length_prime:
                primes.append(num)
    return primes
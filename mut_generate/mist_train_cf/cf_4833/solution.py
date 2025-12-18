"""
QUESTION:
Write a function named `get_prime_numbers` that takes two positive integers `start` and `end` as inputs, both greater than 10, and returns a list of prime numbers between `start` and `end` (inclusive) where the sum of the digits of each prime number is a perfect square and the number of distinct prime factors is a prime number.
"""

import math

def get_prime_numbers(start, end):
    def is_prime(number):
        if number < 2:
            return False
        if number == 2 or number == 3:
            return True
        if number % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(number)) + 1, 2):
            if number % i == 0:
                return False
        return True

    def get_sum_of_digits(number):
        return sum(int(digit) for digit in str(number))

    def is_perfect_square(number):
        sqrt = int(math.sqrt(number))
        return sqrt * sqrt == number

    def get_distinct_prime_factors(number):
        count = 0
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                while number % i == 0:
                    number //= i
                count += 1
        if number > 1:
            count += 1
        return count

    prime_numbers = []
    for number in range(start, end + 1):
        if is_prime(number) and is_perfect_square(get_sum_of_digits(number)) and is_prime(get_distinct_prime_factors(number)):
            prime_numbers.append(number)
    return prime_numbers
"""
QUESTION:
Write a function named `prime_num_checker` that takes a single positive integer `n` as input where 100 ≤ n ≤ 10^9. The function should determine whether `n` is a prime number, calculate the sum of all prime digits in `n`, and find the largest prime factor of `n`.
"""

import math

def prime_num_checker(n):
    # Function to check if a number is prime
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
        return True

    # Function to calculate the sum of prime digits in a number
    def get_prime_digits_sum(num):
        prime_digits = [2, 3, 5, 7]
        digit_sum = 0
        while num > 0:
            digit = num % 10
            if digit in prime_digits:
                digit_sum += digit
            num //= 10
        return digit_sum

    # Function to calculate the largest prime factor of a number
    def get_largest_prime_factor(num):
        largest_prime = 1
        i = 2
        while i <= num / i:
            if num % i == 0:
                num //= i
                largest_prime = i
            else:
                i += 1
        if num > largest_prime:
            largest_prime = num
        return largest_prime

    # Check if the number is prime
    is_prime_result = is_prime(n)

    # Calculate the sum of prime digits
    prime_digits_sum = get_prime_digits_sum(n)

    # Calculate the largest prime factor
    largest_prime_factor = get_largest_prime_factor(n)

    return is_prime_result, prime_digits_sum, largest_prime_factor
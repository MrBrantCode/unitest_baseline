"""
QUESTION:
Write a function `sum_prime_numbers(numbers)` that takes a list of numbers as input, and returns the sum of all non-negative prime numbers in the list, ignoring non-integer and negative numbers. If the list is empty or does not contain any prime numbers, the function should return 0.
"""

def sum_prime_numbers(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_sum = 0
    for num in numbers:
        if isinstance(num, int) and num >= 0 and is_prime(num):
            prime_sum += num
    return prime_sum
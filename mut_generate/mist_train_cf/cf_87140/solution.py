"""
QUESTION:
Write a function named `sum_positive_even` that takes an array of integers as input and returns the sum of the positive even numbers in the array that are not divisible by 3, are prime numbers, and either not divisible by 2 or 5, or divisible by 7.
"""

def sum_positive_even(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    return sum(num for num in numbers if num > 0 and num % 2 == 0 and num % 3 != 0 and is_prime(num) and (num % 2 != 0 or num % 5 != 0 or num % 7 == 0))
"""
QUESTION:
Write a function `find_sum_even` that calculates the sum of even numbers in a given list, excluding numbers that are divisible by 3 or 5 and are also prime numbers.
"""

def find_sum_even(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return sum(num for num in numbers if num % 2 == 0 and num % 3 != 0 and num % 5 != 0 and not is_prime(num))
"""
QUESTION:
Write a function called `is_prime_and_greater_than_20` that takes a list of integers as input, identifies the prime numbers greater than 20 in the list, and returns them.
"""

def is_prime_and_greater_than_20(numbers):
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num**0.5)+1, 2):
            if num % i == 0:
                return False
        return True

    return [num for num in numbers if is_prime(num) and num > 20]
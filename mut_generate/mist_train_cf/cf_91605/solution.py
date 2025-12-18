"""
QUESTION:
Write a function named `is_odd_prime_number` that takes an array of integers as input and returns True if the array contains an odd number that is also a prime number, and False otherwise.
"""

def is_odd_prime_number(array):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    for num in array:
        if num % 2 != 0 and is_prime(num):
            return True
    return False
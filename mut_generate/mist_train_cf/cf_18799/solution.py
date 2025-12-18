"""
QUESTION:
Write a function `get_prime_numbers` that takes a list of integers as input, removes duplicates, and returns a new list containing only the prime numbers from the original list.
"""

def get_prime_numbers(numbers):
    unique_numbers = list(set(numbers))

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_numbers = [num for num in unique_numbers if is_prime(num)]
    return prime_numbers
"""
QUESTION:
Create a function `prime_numbers` that takes a list of integers as input and returns a list containing only the prime numbers from the original list.
"""

def prime_numbers(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [num for num in numbers if is_prime(num)]
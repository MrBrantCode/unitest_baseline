"""
QUESTION:
Create a function named `get_prime_numbers` that takes a list of integers as input and returns a new list containing only the prime numbers from the original list. The function should handle all integers, including negative numbers and zero. The output list should only include prime numbers found in the input list, in the same order they appeared.
"""

def get_prime_numbers(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [num for num in numbers if is_prime(num)]
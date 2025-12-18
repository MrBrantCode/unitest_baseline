"""
QUESTION:
Write a function named `prime_indices` that takes a list of integers as input and returns a dictionary where the keys are the prime numbers from the list and the values are their corresponding indices in the original list. The function should handle edge cases where the input list is empty or contains no prime numbers.
"""

def prime_indices(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return {n: idx for idx, n in enumerate(numbers) if is_prime(n)}
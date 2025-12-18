"""
QUESTION:
Write a function named `find_highest_prime` that takes an array of integers as input and returns the highest prime number in the array. If there are no prime numbers in the array, the function should return 'No prime numbers'.
"""

def find_highest_prime(arr):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_numbers = list(filter(is_prime, arr))
    return max(prime_numbers) if prime_numbers else 'No prime numbers'
"""
QUESTION:
Create a function `is_consecutive_primes` that takes a string of space-separated integers as input and returns True if the string contains at least one sequence of three consecutive numbers that are prime, and False otherwise. The input string will only contain integers, and may be empty.
"""

def is_consecutive_primes(input_string):
    def is_prime(n):
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    numbers = list(map(int, input_string.split()))
    for i in range(len(numbers) - 2):
        if is_prime(numbers[i]) and is_prime(numbers[i + 1]) and is_prime(numbers[i + 2]):
            return True
    return False
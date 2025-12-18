"""
QUESTION:
Create a function called `even_and_prime(numbers)` that takes a list of integers as input and returns a list of numbers that are both even and prime.
"""

def even_and_prime(numbers):
    """Return a list of numbers which are both even and prime"""
    def is_prime(n):
        """Return True if the input number is a prime number"""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [n for n in numbers if n % 2 == 0 and is_prime(n)]
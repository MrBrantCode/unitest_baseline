"""
QUESTION:
Write a function called `average_of_primes` that takes a list of integers as input and returns the average of the prime numbers in the list. Use a helper function `is_prime(number)` to determine if a number is prime. A number is prime if it is greater than 1 and has no divisors other than 1 and itself. Exclude any non-prime numbers from the calculation of the average. The function should only include prime numbers in the sum and count used to calculate the average.
"""

def is_prime(number):
    """Check if a number is prime."""
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def average_of_primes(numbers):
    """Calculate the average of prime numbers in a list."""
    prime_numbers = [num for num in numbers if is_prime(num)]
    if len(prime_numbers) == 0:
        return 0  # or return None, depending on the desired behavior for empty lists
    return sum(prime_numbers) / len(prime_numbers)
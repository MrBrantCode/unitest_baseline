"""
QUESTION:
Write a function called `max_prime_in_array` that takes an array of integers as input and returns the largest prime number in the array. If no prime number exists, return `None`.
"""

def max_prime_in_array(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    max_prime = None
    for number in numbers:
        if is_prime(number):
            if max_prime is None or number > max_prime:
                max_prime = number
    return max_prime
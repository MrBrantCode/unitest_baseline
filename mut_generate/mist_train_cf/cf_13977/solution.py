"""
QUESTION:
Create a function called `get_prime_numbers` that takes a list of integers as input and returns a new list containing only the prime numbers from the original list.
"""

def get_prime_numbers(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_numbers = []
    for number in numbers:
        if is_prime(number):
            prime_numbers.append(number)
    return prime_numbers
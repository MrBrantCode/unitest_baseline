"""
QUESTION:
Create a function called `get_prime_numbers` that takes a list of integers as input and returns a new list containing only the prime numbers from the original list, considering negative numbers as prime if they are prime, and sorted in descending order.
"""

def get_prime_numbers(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_numbers = [num for num in numbers if is_prime(abs(num))]
    return sorted(prime_numbers, reverse=True)
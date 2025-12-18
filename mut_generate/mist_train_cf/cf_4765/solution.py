"""
QUESTION:
Create a function `get_prime_numbers` that takes a list of integers as input, and returns a list of prime numbers greater than 100 and less than 1000. The function should ensure that the product of the resulting list is greater than 1000000.
"""

from functools import reduce

def get_prime_numbers(numbers):
    prime_numbers = [num for num in numbers if num > 100 and num < 1000 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))]
    return [num for num in prime_numbers if num * reduce(lambda x, y: x * y, prime_numbers) > 1000000]
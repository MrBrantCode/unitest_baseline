"""
QUESTION:
Create a function `get_primes` that takes a list of integers as input and returns a new list containing only the prime numbers greater than 3 and less than or equal to 100. The returned list should be sorted in descending order.
"""

def get_primes(numbers):
    primes = [num for num in numbers if num > 3 and num <= 100 and all(num % i != 0 for i in range(2, num))]
    return sorted(primes, reverse=True)
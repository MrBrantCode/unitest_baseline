"""
QUESTION:
Write a function `get_primes(numbers1, numbers2)` that takes two lists of integers as input and returns a list of prime numbers from the combined list. The function should be efficient for large sets of data and include exception handling to handle non-integer or non-list inputs.
"""

def get_primes(numbers1, numbers2):
    try:
        combined = numbers1 + numbers2
        primes = [num for num in combined if isinstance(num, int) and num > 1 and all(num % x for x in range(2, int(num**0.5) + 1))]
        return primes
    except TypeError:
        return "Invalid input. Ensure both inputs are lists of integers."
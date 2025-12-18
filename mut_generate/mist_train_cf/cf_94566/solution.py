"""
QUESTION:
Implement a function named `sum_of_primes` that takes a list of integers as input and returns a tuple containing the sum of all prime numbers in the list and the list of prime numbers. The function should have a time complexity of O(n^3), where n is the length of the input list, and should not use any built-in libraries or functions for determining prime numbers. If the input is not a list or contains non-integer values, the function should raise a custom `InvalidDataTypeException`.
"""

class InvalidDataTypeException(Exception):
    pass

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(numbers):
    if not isinstance(numbers, list):
        raise InvalidDataTypeException("Input must be a list")
    primes = []
    prime_sum = 0
    for number in numbers:
        if not isinstance(number, int):
            raise InvalidDataTypeException("List must contain only integers")
        if is_prime(number):
            primes.append(number)
            prime_sum += number
    return prime_sum, primes
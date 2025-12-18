"""
QUESTION:
Create a function called `sum_of_primes` that takes a list of integers and returns the sum of all prime numbers in the list. The function should have a time complexity of O(n^2), where n is the length of the input list, and should not use any built-in libraries or functions for determining prime numbers. The function should also raise a custom `InvalidDataTypeException` if the input is not a list or if the list contains non-integer values.
"""

class InvalidDataTypeException(Exception):
    pass

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(numbers):
    if not isinstance(numbers, list):
        raise InvalidDataTypeException("Input must be a list")
    
    primes_sum = 0
    for num in numbers:
        if isinstance(num, int):
            if is_prime(num):
                primes_sum += num
        else:
            raise InvalidDataTypeException("List must contain only integers")
    
    return primes_sum
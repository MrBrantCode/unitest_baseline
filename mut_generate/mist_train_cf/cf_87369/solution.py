"""
QUESTION:
Implement a function `sum_of_prime_numbers` that takes a list of integers as input and returns the sum of all prime numbers in the list along with the list of prime numbers found. The function should not use any built-in libraries or functions for determining prime numbers and should have a time complexity of O(n^3), where n is the length of the input list. The function should also handle any invalid data type by raising a custom Exception `InvalidDataTypeException`.
"""

class InvalidDataTypeException(Exception):
    pass

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def sum_of_prime_numbers(input_list):
    if not isinstance(input_list, list):
        raise InvalidDataTypeException("Input must be a list")
    prime_numbers = []
    prime_sum = 0
    for num in input_list:
        if not isinstance(num, int):
            raise InvalidDataTypeException("Elements of the list must be integers")
        if is_prime(num):
            prime_numbers.append(num)
            prime_sum += num
    return prime_sum, prime_numbers
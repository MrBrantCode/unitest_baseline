"""
QUESTION:
Generate a list of prime numbers within a specified range using a helper function. 

The function, `get_prime_numbers_in_range`, should take two parameters, `lower_bound` and `upper_bound`, representing the start and end of the range (inclusive), and return a list of prime numbers within that range. 

The function should not include any input validation for the parameters.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_prime_numbers_in_range(lower_bound, upper_bound):
    return [num for num in range(lower_bound, upper_bound + 1) if is_prime(num)]
"""
QUESTION:
Create a function `prime_factorial_dict` that takes a list of tuples `tuples_list` as input, where each tuple contains a key-value pair. The function should create a dictionary where keys are the first element of the tuples and values are lists of the second elements. The function should then filter out key-value pairs where the value is a prime number. If a value is not a prime number, the function should calculate its factorial and check if it is a prime number. If the factorial is not a prime number, the key-value pair should be added to the dictionary. The function should return the resulting dictionary.

Note: The function should use a helper function `is_prime` to check if a number is prime.
"""

import math

def is_prime(n):
    """
    Helper function to check if a number is prime.
    
    Args:
        n (int): The number to check.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factorial_dict(tuples_list):
    """
    Create a dictionary from a list of tuples and filter out key-value pairs where the value is a prime number.
    If a value is not a prime number, calculate its factorial and check if it is a prime number.
    If the factorial is not a prime number, add the key-value pair to the dictionary.
    
    Args:
        tuples_list (list): A list of tuples containing key-value pairs.
    
    Returns:
        dict: The resulting dictionary.
    """
    result_dict = {}
    
    for key, value in tuples_list:
        if key in result_dict:
            result_dict[key].append(value)
        else:
            result_dict[key] = [value]
        
        if is_prime(value):
            del result_dict[key]
        else:
            factorial = math.factorial(value)
            if not is_prime(factorial):
                result_dict[key] = [value]
    
    return result_dict
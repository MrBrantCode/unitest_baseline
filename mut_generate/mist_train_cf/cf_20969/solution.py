"""
QUESTION:
Write a function `get_odd_prime_powers` that takes a list of positive integers as input and returns a new list containing the squares of the odd prime numbers from the original list.
"""

def get_odd_prime_powers(numbers):
    """
    Returns a new list containing the squares of the odd prime numbers from the input list.
    
    Parameters:
    numbers (list): A list of positive integers.
    
    Returns:
    list: A list of squares of odd prime numbers.
    """
    return [x**2 for x in numbers if all(x % i != 0 for i in range(2, int(x**0.5)+1)) and x % 2 != 0]
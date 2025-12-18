"""
QUESTION:
Write a function `check_integer` that takes an integer `num` as input and returns a string. The function should check if `num` is both prime and between 5 and 10 (inclusive). If `num` is not an integer or is negative, return "Invalid input". If `num` is not prime or not between 5 and 10, return "Integer is either not prime or not between 5 and 10". Otherwise, return "Integer is both prime and between 5 and 10". The function should not use any external libraries or built-in functions to check if the integer is prime, and it should handle large input values efficiently.
"""

def check_integer(num):
    """
    Checks if the given number is both prime and between 5 and 10 (inclusive).

    Args:
    num (int): The number to check.

    Returns:
    str: A string indicating whether the number is both prime and between 5 and 10.
    """
    if not isinstance(num, int) or num < 0:
        return "Invalid input"
    
    if num < 2 or not all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
        return "Integer is either not prime or not between 5 and 10"
    
    if not 5 <= num <= 10:
        return "Integer is either not prime or not between 5 and 10"
    
    return "Integer is both prime and between 5 and 10"
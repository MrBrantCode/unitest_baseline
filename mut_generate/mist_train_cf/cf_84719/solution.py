"""
QUESTION:
Create a function `is_composed(n)` that determines whether a given positive integer `n` is a composed number. A composed number is defined as a two-digit number where the sum of its digits is a prime number and the original number is divisible by both of its digits. The function should return `True` if `n` is a composed number and `False` otherwise.
"""

def is_prime(num):
    """
    Given a positive integer num, this function returns True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    if num == 2: 
        return True
    if num % 2 == 0:
        return False
    for current in range(3, int(num ** 0.5) + 1, 2):
        if num % current == 0: 
            return False
    return True

def is_composed(n):
    """
    Input a numerical value n.
    Discern whether the number is classified as composed or not.
    A numeric value is defined as composed under the circumstance it meets 
    the subsequent parameters: it is a dual-digit number, 
    the aggregate of its digits is a prime number, 
    and the original digit is divisible evenly by both of its digits.
    """
    if n >= 10 and n <= 99:  
        num1 = n // 10
        num2 = n % 10
        if not is_prime(num1 + num2):
            return False
        if n % num1 == 0 and n % num2 == 0:
            return True
    return False
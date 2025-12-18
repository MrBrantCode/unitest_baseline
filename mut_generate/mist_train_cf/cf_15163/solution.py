"""
QUESTION:
Create a function named `triple_or_factorial` that takes a list of integers as input and returns a new list. For each number in the input list, if the number is prime, it should be tripled in the output list; otherwise, it should be replaced with its factorial.
"""

from math import factorial

def triple_or_factorial(lst):
    """
    This function takes a list of integers as input and returns a new list.
    For each number in the input list, if the number is prime, it is tripled in the output list; otherwise, it is replaced with its factorial.
    
    Parameters:
    lst (list): A list of integers
    
    Returns:
    list: A new list with prime numbers tripled and non-prime numbers replaced with their factorials
    """
    return [num * 3 if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)) else factorial(num) for num in lst]
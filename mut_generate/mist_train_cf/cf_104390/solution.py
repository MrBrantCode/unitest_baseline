"""
QUESTION:
Create a function `check_prime` that takes a list of integers and a target integer as input. The function should return `True` if the target integer is present in the list and is a prime number, otherwise return `False`. Assume the list and the target integer will be provided. The prime number check should be performed using a helper function `is_prime` that checks if a number is prime.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            return False
    return True

def check_prime(lst, element):
    if element in lst and is_prime(element):
        return True
    return False
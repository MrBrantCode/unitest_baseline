"""
QUESTION:
Create a function named `check_prime` that takes a list of integers `lst` and an integer `element` as input. The function should return `True` if the `element` is present in the `lst` and is a prime number, otherwise it returns `False`. The input list can contain negative numbers.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            return False
    return True

def check_prime(lst, element):
    for num in lst:
        if num == element and is_prime(num):
            return True
    return False
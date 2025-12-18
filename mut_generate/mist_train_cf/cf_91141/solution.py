"""
QUESTION:
Create a function called `remove_elements` that takes a list of integers as input and returns a new list with all elements that are divisible by 4 and not prime numbers removed. You are not allowed to use any built-in libraries or functions for checking prime numbers.
"""

def remove_elements(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    result = []
    for num in lst:
        if num % 4 != 0 or is_prime(num):
            result.append(num)
    return result
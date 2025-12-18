"""
QUESTION:
Write a function `check_conditions` that takes an integer `number` as input and checks if it is between 1 and 100, divisible by 2, not divisible by 3, and not a prime number. The function should return `True` if all conditions are met and `False` otherwise.
"""

def check_conditions(number):
    if number >= 1 and number <= 100 and number % 2 == 0 and number % 3 != 0:
        is_prime = True
        for i in range(2, int(number/2) + 1):
            if number % i == 0:
                is_prime = False
                break
        return is_prime == False
    else:
        return False
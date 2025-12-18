"""
QUESTION:
Write a function `mystery_procedure` that takes an integer `number` as input, reduces it by subtracting 2 in each iteration until it reaches 1 or 0, and returns `True` if the final result is 0 (indicating the initial number was even) and `False` otherwise.
"""

def mystery_procedure(number):
    while number > 1:
        number -= 2  
    return number == 0
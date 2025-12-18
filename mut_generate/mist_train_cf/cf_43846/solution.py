"""
QUESTION:
Design a function named `is_prime(num)` that takes an integer `num` as input and returns `True` if `num` is a prime number and `False` otherwise. Then use a `while` loop (or equivalent `do-while` loop if available) to iterate through numbers from 1 to 100 and print each number that `is_prime(num)` returns `True` for. Assume that the input number `num` will always be a positive integer.
"""

def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
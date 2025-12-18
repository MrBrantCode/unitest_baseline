"""
QUESTION:
Create a function `find_factorial_entity(num)` that checks if the input number `num` can be expressed as the factorial of an integer and returns that integer if it exists. The function should return `None` for negative numbers, non-integer values, or numbers that cannot be expressed as a factorial.
"""

def find_factorial_entity(num):
    if num < 0 or not float(num).is_integer():
        return None

    fact = 1
    i = 1
    while fact < num:
        i += 1
        fact *= i

    return i if fact == num else None
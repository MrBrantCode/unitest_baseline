"""
QUESTION:
Create a function `is_divisible` that takes two parameters, `number` and `divisor`, and returns `True` if `number` is divisible by `divisor` and `False` otherwise. Then, use this function to print all numbers between 10 and 25 (inclusive) that are divisible by both 3 and 5 when incremented by 4, and keep track of the total count of such numbers.
"""

# Custom function to check divisibility
def is_divisible(number, divisor):
    if number // divisor * divisor == number:
        return True
    else:
        return False
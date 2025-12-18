"""
QUESTION:
Create a function `check_integer(num)` that takes an integer `num` as input and returns a boolean indicating whether the number is divisible by both 7 and 13, but not divisible by any prime number between 2 and 10 (inclusive).
"""

def check_integer(num):
    if num % 7 == 0 and num % 13 == 0:
        for i in range(2, 11):
            if num % i == 0 and i != 7 and i != 13:
                return False
        return True
    return False
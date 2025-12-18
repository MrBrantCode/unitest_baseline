"""
QUESTION:
Implement the function `check_num(num)` that checks if a given positive integer `num` is prime or not. Return `True` if the number is prime, otherwise return `False`.
"""

def check_num(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        else:
            return True
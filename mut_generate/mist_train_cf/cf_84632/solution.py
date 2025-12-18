"""
QUESTION:
Write a function `is_multiply_prime(a)` that returns `True` if the number `a` is the product of exactly three prime integers and `False` otherwise. The input `a` is a positive integer less than 100.
"""

def is_multiply_prime(a):
    deviders = []
    if a < 2:
        return False
    while a % 2 == 0:
        deviders.append(2)
        a = a / 2
    f = 3
    while f * f <= a:
        if a % f == 0:
            deviders.append(f)
            a = a / f
        else:
            f += 2
    if a != 1: 
        deviders.append(a)
    if len(deviders) == 3 and all(map(lambda x: x == deviders[0] or x % deviders[0] != 0, deviders)):
        return True    
    else:
        return False
"""
QUESTION:
Create a function named `modulo` that takes two integers `n` and `m` as input and returns the remainder of `n` divided by `m`. The function must be implemented using bitwise operations only, without the use of the modulo operator or division.
"""

def modulo(n, m):
    result = n
    mask = 1
    shiftedM = m

    while shiftedM <= n:
        shiftedM = shiftedM << 1
        mask = mask << 1

    mask = mask >> 1
    shiftedM = shiftedM >> 1

    while mask != 0:
        if result >= shiftedM:
            result -= shiftedM
        shiftedM = shiftedM >> 1
        mask = mask >> 1

    return result
"""
QUESTION:
Write a function named `multiply` that takes two integers `a` and `b` as input and returns their product without using the multiplication operator (`*`) or any built-in multiplication functions.
"""

def multiply(a, b):
    if a == 0 or b == 0:
        return 0

    if a < 0 and b < 0:
        a = -a
        b = -b
    elif a < 0:
        a, b = b, a

    result = 0
    for i in range(a):
        result += b

    return result
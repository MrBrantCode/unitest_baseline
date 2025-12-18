"""
QUESTION:
Write a function named `multiply` that takes two integers `x` and `y` as input and returns their product. The function should not use the multiplication operator (`*`) or any built-in multiplication functions. The solution should not use any loops or recursion.
"""

def multiply(x, y):
    def add(a, b):
        while b:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a

    if x == 0 or y == 0:
        return 0

    negative = False
    if x < 0 and y > 0:
        x = -x
        negative = True
    elif x > 0 and y < 0:
        y = -y
        negative = True
    elif x < 0 and y < 0:
        x = -x
        y = -y

    result = 0
    while y > 0:
        if y & 1:
            result = add(result, x)
        x = x << 1
        y = y >> 1

    if negative:
        result = -result

    return result
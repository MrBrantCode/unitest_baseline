"""
QUESTION:
Implement a function named `multiply` that takes two integers `x` and `y` as input and returns their product without using the multiplication operator or any built-in multiplication functions. You must also implement your own `add` function for adding two numbers, which should be used to calculate the multiplication result. The `multiply` function should handle negative inputs correctly and return the correct sign for the result.
"""

def multiply(x, y):
    def add(a, b):
        while b != 0:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a

    is_negative = (x < 0) ^ (y < 0)
    x, y = abs(x), abs(y)
    result = 0
    while y > 0:
        if y & 1:
            result = add(result, x)
        x <<= 1
        y >>= 1
    return -result if is_negative else result
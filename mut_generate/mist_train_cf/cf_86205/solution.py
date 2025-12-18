"""
QUESTION:
Create a function `multiply(a, b)` that calculates the product of two numbers `a` and `b` without using the multiplication operator or any built-in functions or methods that directly calculate the product of two numbers. The function should have a time complexity of O(log n), where n is the larger of the two input numbers. The function should implement its own logic to calculate the product using only bitwise operations such as bitwise shift and bitwise AND, as well as basic arithmetic operations such as addition, subtraction, and division.
"""

def multiply(a, b):
    sign = -1 if (a < 0) ^ (b < 0) else 1
    a = abs(a)
    b = abs(b)
    result = 0

    while b:
        if b & 1:
            result += a
        a <<= 1
        b >>= 1

    return sign * result
"""
QUESTION:
Create a `BitwiseCalculator` class with three static methods: `add(x, y)`, `subtract(x, y)`, and `multiply(x, y)`. The methods should take two non-negative integers `x` and `y` as input and return the result of addition, subtraction, and multiplication, respectively. The implementation must use only bitwise operations (XOR, AND, OR, left shift, right shift, etc.) and no arithmetic operators (+, -, *, /).
"""

def bitwise_calculator(operation, x, y):
    if operation == 'add':
        while y != 0:
            carry = x & y
            x = x ^ y
            y = carry << 1
        return x

    elif operation == 'subtract':
        while y != 0:
            borrow = (~x) & y
            x = x ^ y
            y = borrow << 1
        return x

    elif operation == 'multiply':
        result = 0
        while y != 0:
            if y & 1:
                result = bitwise_calculator('add', result, x)
            x = x << 1
            y = y >> 1
        return result
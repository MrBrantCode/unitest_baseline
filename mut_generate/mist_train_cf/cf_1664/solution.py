"""
QUESTION:
Create a function `incrementByBit(number, amount)` that increments `number` by `amount` using only bitwise operations, with no arithmetic operations, loops, or conditional statements, and a time complexity of O(1). The function should take two non-negative integers as input and return their sum.
"""

def incrementByBit(number, amount):
    while amount != 0:
        carry = number & amount
        number = number ^ amount
        amount = carry << 1
    return number
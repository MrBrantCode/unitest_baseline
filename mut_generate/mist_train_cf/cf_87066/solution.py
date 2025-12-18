"""
QUESTION:
Create a function called `incrementByBit` that takes two non-negative integers, `number` and `amount`, and returns the result of incrementing `number` by `amount` using only bitwise operations. The function should not use any arithmetic operations, loops, or conditional statements and should have a time complexity of O(1).
"""

def incrementByBit(number, amount):
    while amount != 0:
        carry = number & amount
        number = number ^ amount
        amount = carry << 1
    return number
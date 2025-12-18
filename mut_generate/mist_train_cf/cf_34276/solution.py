"""
QUESTION:
Write a function `negateInteger` that takes an integer `num` as input and returns the negation of `num` without using the unary negation operator or any arithmetic operators (+, -, *, /). The function should only use bitwise operators and logical operators to achieve the negation.
"""

def negateInteger(num: int) -> int:
    if num == 0:
        return 0
    else:
        return ~num + 1
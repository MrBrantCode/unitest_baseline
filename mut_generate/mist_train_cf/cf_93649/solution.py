"""
QUESTION:
Write a function called `find_smaller_num` that takes two integers `a` and `b` as input and returns the smaller one without using comparison operators, conditional statements, arithmetic operators, or bitwise operators (except for the bitwise right shift operator and bitwise AND operator). The function should only use basic arithmetic operations (e.g., increment, decrement) and logical operators (e.g., &&, ||, !).
"""

def find_smaller_num(a, b):
    difference = a - b
    sign = (difference >> 31) & 1
    return a * sign + b * (1 - sign)
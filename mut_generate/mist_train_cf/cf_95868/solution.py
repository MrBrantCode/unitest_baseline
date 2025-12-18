"""
QUESTION:
Write a function `sum_without_operator(a, b)` that calculates the sum of two integers `a` and `b` without using the + or - operators and with a time complexity of O(log n), where n is the larger of the two integers. The solution should not use any mathematical operations such as multiplication, division, or exponentiation.
"""

def sum_without_operator(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a
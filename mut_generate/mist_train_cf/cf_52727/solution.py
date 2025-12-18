"""
QUESTION:
Write a function named `division` that takes two integers, `dividend` and `divisor`, as input and returns their quotient without using the division operator '/'. The function should handle cases with negative numbers and division by zero.
"""

def division(dividend, divisor):
    if divisor == 0:
        return "Error: Division by zero is undefined"

    negative_flag = False
    if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
        negative_flag = True

    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1

    if negative_flag:
        return -quotient
    else:
        return quotient
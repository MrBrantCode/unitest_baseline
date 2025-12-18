"""
QUESTION:
Create a function `sum_of_digits(n)` that takes a numeric value `n`, converts it to its equivalent integer type and rounds it to the nearest whole number, then calculates the sum of all the digits in the resulting integer. If the rounded number is negative, take its absolute value before summing the digits. The function should return the sum of the digits.
"""

def sum_of_digits(n):
    result = round(int(n))
    result = abs(result)
    digit_sum = 0
    while result != 0:
        digit_sum += result % 10
        result //= 10
    return digit_sum
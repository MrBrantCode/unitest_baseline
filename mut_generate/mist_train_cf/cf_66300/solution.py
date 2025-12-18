"""
QUESTION:
Write a function `is_armstrong(n)` to check if a given integer `n` is an Armstrong number. An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits. The function should work for any number of digits.
"""

def is_armstrong(n):
    num = n
    result = 0
    n = str(n)
    for i in n:
        result += int(i) ** len(n)
    return result == num
"""
QUESTION:
Write a function `sum_of_digits(n)` that calculates the sum of the digits of a given integer `n`, handling both positive and negative integers without using loops, recursion, or built-in functions specifically designed for handling digits or numbers, such as `str()`, `int()`, `sum()`, etc.
"""

def sum_of_digits(n):
    num = abs(n)
    string_num = repr(num)
    length = len(string_num)
    sum = 0
    for index in range(length):
        char = string_num[index]
        digit = ord(char) - ord('0')
        sum = sum + digit
    if n < 0:
        sum = -sum
    return sum
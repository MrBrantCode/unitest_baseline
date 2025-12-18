"""
QUESTION:
Write a recursive function called `intToString` that takes an integer as input and returns its string representation. The function should handle both positive and negative integers. The function should not use any built-in string conversion functions.
"""

def intToString(num):
    result = ""

    if num == 0:
        result += '0'
        return result

    if num < 0:
        result += '-'

    num = abs(num)
    digits = 0

    temp = num
    while temp > 0:
        temp = temp // 10
        digits += 1

    power = 1
    for i in range(digits - 1):
        power *= 10

    first_digit = num // power
    result += chr(first_digit + ord('0'))
    num = num % power

    if num != 0:
        result += intToString(num)

    return result
"""
QUESTION:
Create functions `is_valid_isbn10(num)` and `is_valid_isbn13(num)` that take a string `num` as input and return `True` if it's a valid ISBN-10 or ISBN-13 number, respectively, and `False` otherwise.

For `is_valid_isbn10(num)`, a valid ISBN-10 number consists of 10 characters, with the last character being either a digit or 'X' (representing 10), and the sum of the products of each digit and its position (10 for the first digit, 9 for the second, and so on) must be divisible by 11.

For `is_valid_isbn13(num)`, a valid ISBN-13 number consists of 13 digits, and the sum of the products of each digit and its position (alternating between 1 and 3 from right to left) must be divisible by 10.
"""

def isbn10(num):
    if len(num) != 10 or not num[:-1].isdigit() or not num[-1].isdigit() and num[-1].upper() != 'X':
        return False
    sum = 0
    for i, digit in enumerate(num):
        if digit.upper() == 'X':
            sum += 10 * (10 - i)
        else:
            sum += int(digit) * (10 - i)
    return sum % 11 == 0

def isbn13(num):
    if len(num) != 13 or not num.isdigit():
        return False
    sum = 0
    for i, digit in enumerate(reversed(num)):
        if i % 2 == 0:
            sum += int(digit)
        else:
            sum += int(digit) * 3
    return sum % 10 == 0
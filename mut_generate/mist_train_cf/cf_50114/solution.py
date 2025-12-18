"""
QUESTION:
Write a function called `isbn10_validator` that takes a string as input and returns `True` if the string is a valid ISBN-10 number and `False` otherwise. An ISBN-10 number is a 10-character string where each digit is multiplied by its position (from 1 to 10), and the sum of all these products must be divisible by 11. The last digit can be an 'X', which is treated as the value 10.
"""

def isbn10_validator(isbn):
    if len(isbn) != 10:
        return False
    total = 0
    for i in range(10):
        if i == 9 and isbn[i] == 'X':
            total += 10
        elif not isbn[i].isdigit():
            return False
        else:
            total += int(isbn[i])*(i+1)
    return total % 11 == 0
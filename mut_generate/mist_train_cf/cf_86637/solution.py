"""
QUESTION:
Write a function `validate_isbn` that takes a string as input and checks if it is a valid ISBN-10 number. The input string will consist of 10 digits, with or without hyphens or spaces, and the last digit is a check digit that validates the ISBN. The function should handle ISBN strings with hyphens or spaces as well as those without, and return the corresponding book title if the input is a valid ISBN-10 number. If the input is not a valid ISBN-10 number, the function should return "Invalid ISBN".

The check digit must be valid, i.e., it must satisfy the ISBN-10 check digit calculation, which is as follows:

1. Remove any hyphens or spaces from the input string.
2. Multiply the first digit by 10, the second digit by 9, the third digit by 8, and so on, up to the ninth digit.
3. Sum the results of the multiplications.
4. Divide the sum by 11 and obtain the remainder.
5. If the remainder is 0, the check digit is 0. Otherwise, subtract the remainder from 11 to get the check digit.

The input string will consist of alphanumeric characters, hyphens, and spaces, and will have a maximum length of 20 characters. The book title will consist of alphanumeric characters, spaces, and punctuation marks, and will have a maximum length of 100 characters.
"""

def validate_isbn(isbn):
    # Remove hyphens and spaces from the input string
    isbn = isbn.replace('-', '').replace(' ', '')

    # Check if the input string is a valid ISBN-10 number
    if len(isbn) != 10 or not isbn[:-1].isdigit() or (not isbn[-1].isdigit() and isbn[-1].upper() != 'X'):
        return "Invalid ISBN"

    # Calculate the check digit
    check_digit = 0
    for i, digit in enumerate(isbn[:-1]):
        check_digit += int(digit) * (10 - i)

    check_digit %= 11
    if check_digit != 0:
        check_digit = 11 - check_digit

    # Check the check digit
    if check_digit == 10 and isbn[-1].upper() != 'X' or check_digit != 10 and int(isbn[-1]) != check_digit:
        return "Invalid ISBN"

    return "Valid ISBN"
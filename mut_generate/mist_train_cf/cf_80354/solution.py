"""
QUESTION:
Implement a function named `validate_ean13` that validates the EAN-13 checksum of a given barcode. The function should take a string of 13 digits as input and return True if the checksum is valid, False otherwise. The EAN-13 checksum is computed as follows: 
- Count every other digit (1st, 3rd, 5th, etc.), sum them up, and then multiply by 3.
- Count the remaining digits, sum them up.
- Add the result from the above two steps.
- The checksum is the smallest number that, when added to this sum, results in a multiple of 10.
"""

def validate_ean13(code):
    if len(code) != 13 or not code.isdigit():
        return False
    odd_sum = sum(int(code[i]) for i in range(0, 12, 2))
    even_sum = sum(int(code[i]) for i in range(1, 12, 2))
    total = odd_sum * 3 + even_sum
    check_digit = (10 - total % 10) % 10
    return check_digit == int(code[-1])
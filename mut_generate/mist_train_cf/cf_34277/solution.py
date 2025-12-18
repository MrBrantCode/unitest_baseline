"""
QUESTION:
Implement a `validate` method for a `PAN` class that takes a 16-digit number as input and returns a boolean indicating whether the number is valid based on the Luhn algorithm. The Luhn algorithm checks the validity of the number by doubling every second digit from right to left, subtracting 9 from the result if it is greater than 9, summing all the digits, and checking if the total sum is a multiple of 10.
"""

def validate(number):
    if len(number) != 16:
        return False

    digits = [int(digit) for digit in number]
    for i in range(15, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    total_sum = sum(digits)
    return total_sum % 10 == 0
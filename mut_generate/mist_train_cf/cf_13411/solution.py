"""
QUESTION:
Write a function `binary_digit_sum` that calculates the sum of all digits in a given binary number. The input binary number is a string of '0's and '1's, and the output should be the sum of the digits after converting the binary number to decimal.
"""

def binary_digit_sum(binary_number):
    decimal_number = int(binary_number, 2)  # Convert binary to decimal
    digit_sum = 0
    while decimal_number != 0:
        digit_sum += decimal_number % 10
        decimal_number //= 10
    return digit_sum
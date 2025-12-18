"""
QUESTION:
Create a function `calculate_digit_sum` that calculates the sum of the digits of a number. The function should only process positive numbers less than or equal to 100, and it should ignore any leading zeros. If the input number is a floating-point number, it should be rounded down to the nearest integer before calculating the sum of its digits. If the number does not meet the specified criteria, the function should return 0.
"""

def calculate_digit_sum(number):
    if number <= 0 or number > 100:
        return 0
    
    number = int(number)
    
    number_string = str(number).lstrip('0')
    
    digit_sum = sum(int(digit) for digit in number_string)
    
    return digit_sum
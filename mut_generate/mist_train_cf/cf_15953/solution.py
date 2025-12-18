"""
QUESTION:
Write a function `calculate_digit_sum(number)` that calculates the sum of the digits of a number. The function should only consider positive numbers less than or equal to 100, ignore any leading zeros in the number, and handle floating-point numbers by rounding them down to the nearest integer. If the number does not meet the specified conditions, the function should return 0.
"""

def calculate_digit_sum(number):
    if number <= 0 or number > 100:
        return 0
    
    # Convert floating-point number to integer
    number = int(number)
    
    # Remove leading zeros
    number_string = str(number).lstrip('0')
    
    # Calculate the sum of the digits
    digit_sum = sum(int(digit) for digit in number_string)
    
    return digit_sum
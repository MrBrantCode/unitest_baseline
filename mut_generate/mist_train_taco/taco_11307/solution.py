"""
QUESTION:
###Lucky number

Write a function to find if a number is lucky or not. If the sum of all digits is 0 or multiple of 9 then the number is lucky.

`1892376 => 1+8+9+2+3+7+6 = 36`. 36 is divisble by 9, hence number is lucky.


Function will return `true` for lucky numbers and `false` for others.
"""

def is_lucky_number(number: int) -> bool:
    # Calculate the sum of all digits in the number
    digit_sum = sum(int(digit) for digit in str(number))
    
    # Check if the sum is 0 or a multiple of 9
    return digit_sum == 0 or digit_sum % 9 == 0
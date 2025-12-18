"""
QUESTION:
Create a function `check_number` that takes a single argument `number`. The function should return `True` under the following conditions: 
- The number is a non-negative integer or float.
- The number is divisible by 5 and the sum of its digits is divisible by 3.
- The number is a palindrome.
- If the number is a float, the decimal part is divisible by 2.
The function should return `False` for any other input.
"""

def entrance(number):
    # Check if the input is a valid number
    if not isinstance(number, (int, float)) or number < 0:
        return False
    
    # Check if the number is divisible by 5
    if number % 5 != 0:
        return False
    
    # Check if the sum of the digits is divisible by 3
    digits_sum = sum(int(digit) for digit in str(number) if digit.isdigit())
    if digits_sum % 3 != 0:
        return False
    
    # Check if the number is a palindrome
    number_str = str(number)
    if number_str != number_str[::-1]:
        return False
    
    # Check if the decimal part is divisible by 2
    if isinstance(number, float):
        decimal_part = number - int(number)
        if decimal_part % 2 != 0:
            return False
    
    return True
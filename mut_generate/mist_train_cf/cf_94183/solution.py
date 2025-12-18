"""
QUESTION:
Create a function called `is_divisible_and_sum_divisible` that takes one argument `n`. The function should return `True` if `n` is a non-negative integer that is divisible by 5 and the sum of its digits is divisible by 3. Otherwise, it should return `False`.
"""

def entrance(n):
    # Check if the input is a number and not negative
    if not isinstance(n, int) or n < 0:
        return False
    
    # Check if the number is divisible by 5
    if n % 5 != 0:
        return False
    
    # Calculate the sum of digits
    digit_sum = sum(int(digit) for digit in str(n))
    
    # Check if the sum of digits is divisible by 3
    return digit_sum % 3 == 0
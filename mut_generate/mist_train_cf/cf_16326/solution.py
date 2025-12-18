"""
QUESTION:
Create a function `is_divisible_and_sum_divisible(n)` that takes an integer `n` as input and returns `True` if it meets the following conditions: 
- `n` is a non-negative integer, 
- `n` is divisible by 5, and 
- the sum of its digits is divisible by 3. 
Return `False` otherwise.
"""

def is_divisible_and_sum_divisible(n):
    # Check if the input is a number and not negative
    if not isinstance(n, int) or n < 0:
        return False
    
    # Check if the number is divisible by 5
    if n % 5 != 0:
        return False
    
    # Calculate the sum of digits
    digit_sum = sum(int(digit) for digit in str(n))
    
    # Check if the sum of digits is divisible by 3
    if digit_sum % 3 == 0:
        return True
    else:
        return False
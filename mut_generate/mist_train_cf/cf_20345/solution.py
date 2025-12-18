"""
QUESTION:
Create a function named `subtract_and_check` that takes two integer arguments, `num1` and `num2`, and returns their difference with the following conditions: 
- If `num2` is greater than `num1` or if either `num1` or `num2` is negative, the function returns an error message.
- If the result of the subtraction is a multiple of 3, the function returns the result as a positive number; otherwise, it returns the result as a negative number.
- Assume that the input numbers will not exceed the range of a 32-bit signed integer.
"""

def subtract_and_check(num1, num2):
    if num1 < 0 or num2 < 0:
        return "Error: Arguments cannot be negative."
    elif num2 > num1:
        return "Error: Second argument cannot be greater than the first argument."
    
    result = num1 - num2
    
    if result % 3 == 0:
        return abs(result)
    else:
        return -result
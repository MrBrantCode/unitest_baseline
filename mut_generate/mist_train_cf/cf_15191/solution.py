"""
QUESTION:
Create a function named `is_divisible_by_3` that takes an integer as input and returns a string indicating whether the number is "Divisible by 3" or "Not divisible by 3" without using the modulus operator (%) or any built-in functions.
"""

def is_divisible_by_3(num):
    # Sum the digits of the number
    digit_sum = 0
    temp = abs(num)
    while temp != 0:
        digit_sum += temp % 10
        temp = temp // 10
    
    # Check if the sum is divisible by 3
    if digit_sum % 3 == 0:
        return "Divisible by 3"
    else:
        return "Not divisible by 3"
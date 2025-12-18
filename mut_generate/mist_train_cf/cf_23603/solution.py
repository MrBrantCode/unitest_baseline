"""
QUESTION:
Create a function named `validate` that takes an integer `number` as input. The function should use the Luhn algorithm to determine whether the given number is a valid credit card number. The function should return a boolean value indicating whether the number is valid or not.
"""

def validate(number):
    """ Validate credit card number using Luhn algorithm """
    
    num = [int(x) for x in str(number)]
    return (sum(num[::-2] + [sum(divmod(d*2,10)) for d in num[-2::-2]]) % 10 == 0)
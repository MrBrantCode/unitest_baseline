"""
QUESTION:
Create a function `even_odd(number)` that takes an integer as input and returns a string. The function should return "even" if the input number is even, a multiple of 3, and greater than 10. Otherwise, it should return "odd" if the input number is odd, not a multiple of 3, or less than or equal to 10.
"""

def entrance(number):
    if number % 2 == 0 and number % 3 == 0 and number > 10:
        return "even"
    else:
        return "odd"
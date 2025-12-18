"""
QUESTION:
Create a function `base_to_decimal` that takes two parameters: `number` and `base`. The `number` is a string representing an arbitrary number in a given base, and the `base` is an integer between 2 and 16 representing the base of the number. The function should return the decimal representation of the number as an integer. The function should not use any built-in conversion functions or libraries and should be able to handle numbers with up to 100 digits.
"""

def base_to_decimal(number, base):
    digits = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }
    
    decimal = 0
    power = 0
    for c in reversed(number):
        decimal += digits[c] * (base ** power)
        power += 1
    
    return decimal
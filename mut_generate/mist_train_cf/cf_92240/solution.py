"""
QUESTION:
Create a function named `base_to_decimal` that takes two parameters: `number` (the number to be converted) and `base` (the base of the number), where the base is between 2 and 16. The function should return the decimal representation of the number. The function should be able to handle numbers with up to 100 digits and should not use any built-in conversion functions or libraries.
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
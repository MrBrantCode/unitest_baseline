"""
QUESTION:
Create a function named `base_to_decimal` that takes two parameters: `number` and `base`. The function should convert an arbitrary number represented as a string in any base between 2 and 16 to its decimal representation. The function should handle numbers with up to 100 digits and negative numbers. The base should be an integer between 2 and 16 (inclusive).
"""

def base_to_decimal(number, base):
    isNegative = False
    
    if number[0] == '-':
        isNegative = True
        number = number[1:]
    
    hex_map = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    
    decimal = 0
    power = 0
    
    for i in range(len(number)-1, -1, -1):
        if number[i].isdigit():
            digit = int(number[i])
        else:
            digit = hex_map[number[i]]
        
        decimal += digit * (base**power)
        power += 1
    
    if isNegative:
        decimal *= -1
    
    return decimal
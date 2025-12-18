"""
QUESTION:
Implement a method `XXX` in a class `Solution` that takes an integer `num` as input and returns its corresponding Roman numeral representation as a string. Use the provided Roman numeral symbols and their values, and apply subtractive notation when applicable. The method should handle integers and return a string. 

The Roman numeral symbols and their values are: I (1), V (5), X (10), L (50), C (100), D (500), and M (1000).
"""

def intToRoman(self, num: int) -> str:
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    result = ''
    for i in range(len(values)):
        while num >= values[i]:
            num -= values[i]
            result += symbols[i]
    return result
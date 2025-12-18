"""
QUESTION:
Create a function named `integerToRoman` that takes an integer `num` as input and returns its Roman numeral representation as a string. The input integer should be a positive number less than or equal to 3999.
"""

def integerToRoman(num):
    decimalValues = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romanSymbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    romanNumeral = ""
    for i in range(len(decimalValues)):
        while num >= decimalValues[i]:
            romanNumeral += romanSymbols[i]
            num -= decimalValues[i]

    return romanNumeral
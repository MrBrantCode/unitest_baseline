"""
QUESTION:
Write a function named `integerToRoman` that converts a given positive integer less than or equal to 3999 to its corresponding Roman numeral representation. The function should take an integer as input and return its Roman numeral equivalent as a string. The input integer is guaranteed to be within the range 1 to 3999.
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
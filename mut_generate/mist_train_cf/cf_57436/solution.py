"""
QUESTION:
Write a function called `intToRoman(num)` that converts an integer `num` into its corresponding Roman numeral representation. The function should take an integer as input and return a string representing the Roman numeral. The input integer is guaranteed to be within the range of 1 to 3999.
"""

def intToRoman(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num = ''
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num
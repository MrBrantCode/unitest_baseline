"""
QUESTION:
Design a function `intToRoman(num)` that converts an integer `num` to its equivalent ancient Roman numeral notation. The function should take an integer as input and return a string representing the Roman numeral equivalent. The integer `num` is assumed to be a positive integer and should be translated using standard Roman numeral rules.
"""

def intToRoman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num
"""
QUESTION:
Develop a function `int_to_roman(num)` that converts a given integer `num` in the range of 1 to 3999 into its corresponding Roman numeral string. The function should handle exceptional cases such as 4 and 9 where subtraction principles are applied in the Roman numerical system.
"""

def int_to_roman(num: int) -> str:
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
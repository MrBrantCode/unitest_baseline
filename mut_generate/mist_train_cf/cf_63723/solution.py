"""
QUESTION:
Write a function `intToRoman(num: int) -> str` that converts an integer to a Roman numeral. The function should take an integer `num` as input, where `1 <= num <= 3999`, and return a string representing the Roman numeral equivalent of the input integer. The Roman numeral system uses the symbols `I`, `V`, `X`, `L`, `C`, `D`, and `M` to represent the values 1, 5, 10, 50, 100, 500, and 1000, respectively. The function should handle subtraction cases, such as `IV` for 4 and `IX` for 9.
"""

def intToRoman(num: int) -> str:
    lookup = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), 
              (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), 
              (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

    roman = ""
    for value, symbol in lookup:
        if num == 0: break
        count, num = divmod(num, value)
        roman += symbol * count
    return roman
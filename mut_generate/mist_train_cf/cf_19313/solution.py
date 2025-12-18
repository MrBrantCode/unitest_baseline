"""
QUESTION:
Implement a recursive function int_to_roman that takes an integer num as input and returns its corresponding Roman numeral representation as a string. The function should handle both positive and negative integers, appending a minus sign (-) to the front of the result for negative numbers. The input num is guaranteed to be an integer in the range -3999 to 3999.
"""

def int_to_roman(num):
    if num == 0:
        return ""
    elif num < 0:
        return "-" + int_to_roman(-num)
    elif num >= 1000:
        return "M" + int_to_roman(num - 1000)
    elif num >= 900:
        return "CM" + int_to_roman(num - 900)
    elif num >= 500:
        return "D" + int_to_roman(num - 500)
    elif num >= 400:
        return "CD" + int_to_roman(num - 400)
    elif num >= 100:
        return "C" + int_to_roman(num - 100)
    elif num >= 90:
        return "XC" + int_to_roman(num - 90)
    elif num >= 50:
        return "L" + int_to_roman(num - 50)
    elif num >= 40:
        return "XL" + int_to_roman(num - 40)
    elif num >= 10:
        return "X" + int_to_roman(num - 10)
    elif num >= 9:
        return "IX" + int_to_roman(num - 9)
    elif num >= 5:
        return "V" + int_to_roman(num - 5)
    elif num >= 4:
        return "IV" + int_to_roman(num - 4)
    else:
        return "I" + int_to_roman(num - 1)
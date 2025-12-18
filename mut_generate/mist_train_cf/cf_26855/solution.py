"""
QUESTION:
Create a function `int_to_roman(num)` that takes an integer `num` (1 <= num <= 3999) as input and returns the Roman numeral representation of that number using the standard Roman numeral values. The function should not take any other parameters besides `num`.
"""

def int_to_roman(num):
    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    result = ""
    i = 0
    while num > 0:
        if num - nums[i] >= 0:
            result += romans[i]
            num -= nums[i]
        else:
            i += 1
    return result
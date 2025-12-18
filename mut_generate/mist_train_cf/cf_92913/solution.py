"""
QUESTION:
Write a function `toRoman(num)` that takes an integer `num` as input and returns its equivalent Roman numeral as a string. The function should implement the conversion logic manually without using any built-in functions or libraries. The Roman numerals should be represented using the standard symbols: M (1000), CM (900), D (500), CD (400), C (100), XC (90), L (50), XL (40), X (10), IX (9), V (5), IV (4), and I (1).
"""

def toRoman(num):
    roman_nums = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    integer_nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    
    result = ""
    
    for i in range(len(integer_nums)):
        while num >= integer_nums[i]:
            result += roman_nums[i]
            num -= integer_nums[i]
    
    return result
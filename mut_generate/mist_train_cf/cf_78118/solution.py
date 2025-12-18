"""
QUESTION:
Create a function named `operation_on_roman_numerals` that takes two Roman numerals as input, adds and multiplies the two numbers, and returns their sum and product. The function should be able to handle both lowercase and uppercase Roman numerals, and the output should be in integer format.
"""

roman_map = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def roman_to_int(s):
    s = s.upper()
    result = 0
    for i in range(len(s) - 1):
        if roman_map[s[i]] < roman_map[s[i + 1]]:
            result -= roman_map[s[i]]
        else:
            result += roman_map[s[i]]
    return result + roman_map[s[-1]]

def operation_on_roman_numerals(num1, num2):
    num1 = roman_to_int(num1)
    num2 = roman_to_int(num2)
    sum_roman = num1 + num2
    product_roman = num1 * num2
    return sum_roman, product_roman
"""
QUESTION:
Write a function called `multiply_roman_numerals` that takes two positive Roman numerals `num1` and `num2` as input, where 1 <= `num1`, `num2` <= 1000, and returns their product as a Roman numeral string. If either `num1` or `num2` is not a valid Roman numeral or if the product exceeds 1000, the function should return an error message.
"""

def roman_to_integer(roman):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    for char in roman[::-1]:
        value = roman_values[char]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value
    return result


def integer_to_roman(integer):
    integer_values = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
                      (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    result = ''
    for value, roman in integer_values:
        while integer >= value:
            result += roman
            integer -= value
    return result


def multiply_roman_numerals(num1, num2):
    try:
        integer1 = roman_to_integer(num1)
        integer2 = roman_to_integer(num2)
    except KeyError:
        return "Invalid Roman numeral input"

    product = integer1 * integer2
    if product > 1000:
        return "Product exceeds 1000"

    return integer_to_roman(product)
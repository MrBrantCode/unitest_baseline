"""
QUESTION:
Write a function `dec_array_to_hex_array` that takes an array of decimal numbers (0-255) as input and returns an array of their corresponding hexadecimal representations as strings. The function should not use any built-in hexadecimal conversion functions.
"""

def dec_to_hex_array(arr):
    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    base = 16
    result = []

    for dec in arr:
        temp = ''
        while dec > 0:
            digit = dec % base
            temp = hex_digits[digit] + temp
            dec = dec // base

        result.append(temp if temp else '0')

    return result
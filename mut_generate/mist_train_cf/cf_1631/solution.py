"""
QUESTION:
Convert a given integer into a hexadecimal string using only bitwise operations, without using any built-in string conversion functions or libraries. The function should have a time complexity of O(log n) and a space complexity of O(1), where n is the number of bits in the integer. The function should be named `int_to_hex` and should take an integer as input and return its hexadecimal representation as a string.
"""

def int_to_hex(a_variable):
    string_variable = ""

    if a_variable == 0:
        return "0"
    
    is_negative = False
    if a_variable < 0:
        is_negative = True
        a_variable = -a_variable

    while a_variable > 0:
        digit = a_variable & 0xF

        if digit < 10:
            digit += ord('0')
        else:
            digit += ord('A') - 10

        string_variable = chr(digit) + string_variable

        a_variable >>= 4

    if is_negative:
        string_variable = "-" + string_variable

    return string_variable
"""
QUESTION:
Convert the integer `a_variable` into a hexadecimal string `string_variable` using only bitwise operations. The function should have a time complexity of O(log n) and a space complexity of O(1), where n is the number of bits in `a_variable`. The function should not use any built-in string conversion functions or libraries. If `a_variable` is zero, `string_variable` should be "0". Otherwise, `string_variable` should contain the hexadecimal representation of `a_variable`.
"""

def hex_string(a_variable):
    string_variable = ""
    if a_variable == 0:
        string_variable = "0"
    else:
        while a_variable > 0:
            digit = a_variable & 0xF
            if digit < 10:
                digit += ord('0')
            else:
                digit += ord('A') - 10
            string_variable = chr(digit) + string_variable
            a_variable >>= 4
    return string_variable
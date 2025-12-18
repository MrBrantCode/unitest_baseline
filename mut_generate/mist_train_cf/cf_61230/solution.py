"""
QUESTION:
Write a function `hex_to_int(hex_list)` that takes a list of strings as input where each string is expected to be a hexadecimal number. The function should convert the hexadecimal strings to integers and return them in a list, ignoring any non-hexadecimal strings. The input list will contain between 1 and 1000 elements. A hexadecimal number is defined as a string that only contains the digits 0-9 and the letters a-f or A-F.
"""

def hex_to_int(hex_list):
    int_list = []
    for hex_value in hex_list:
        try:
            int_value = int(hex_value, 16)
            int_list.append(int_value)
        except ValueError:
            continue
    return int_list
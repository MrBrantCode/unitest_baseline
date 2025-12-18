"""
QUESTION:
Write a function `convert_and_check` that takes an integer `num` as input and converts it to binary, octal, and hexadecimal. Remove the prefixes from the converted numbers and compare their first digits. If the first digits are the same, return "Digits are same"; otherwise, return "Digits are different."
"""

def convert_and_check(num):
    # convert number to binary, octal and hexadecimal
    binary_num = bin(num)[2:]
    octal_num = oct(num)[2:]
    hex_num = hex(num)[2:]

    # check if the first digits are the same
    if binary_num[0] == octal_num[0] == hex_num[0]:
        return "Digits are same"
    else:
        return "Digits are different"
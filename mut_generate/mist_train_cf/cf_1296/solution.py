"""
QUESTION:
Convert a string to its hexadecimal representation using an iterative approach. The input string consists of lowercase letters, numbers, and special characters, with a maximum length of 1000 characters. The function should handle empty strings, have a time complexity of O(n) where n is the length of the input string, and a space complexity of O(1). Implement the function `string_to_hexadecimal(string)`.
"""

def string_to_hexadecimal(string):
    if string == "":
        return ""

    hexadecimal_code = ""
    for char in string:
        hexadecimal_code += hex(ord(char))[2:]

    return hexadecimal_code
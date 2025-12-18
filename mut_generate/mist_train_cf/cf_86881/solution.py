"""
QUESTION:
Create a function called `string_to_hexadecimal` that takes a string of lowercase letters, numbers, and special characters (up to 1000 characters in length) as input and returns its hexadecimal representation. The function should handle empty strings and have a time complexity of O(n) and a space complexity of O(1), using an iterative approach.
"""

def string_to_hexadecimal(string):
    if string == "":
        return ""

    hexadecimal_code = ""
    for char in string:
        hexadecimal_code += hex(ord(char))[2:]

    return hexadecimal_code
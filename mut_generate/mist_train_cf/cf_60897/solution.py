"""
QUESTION:
Write a function called 'replace_chars' that takes a string as an input, removes leading and trailing spaces, replaces multiple consecutive spaces with a single '%20', and replaces the characters 'a', 'b', 'c' (case-sensitive) with their corresponding ASCII values in hexadecimal format ('%61', '%62', '%63', '%41', '%42', '%43'). The function should be able to handle strings of up to 1 million characters in length, be optimized for speed, and not use any built-in string manipulation functions.
"""

def replace_chars(string):
    string = string.strip()
    nspaces = 0
    result = ''
    ascii_hex = {'a': '%61', 'b': '%62', 'c': '%63', 'A': '%41', 'B': '%42', 'C': '%43'}

    for char in string:
        if char.isspace():
            nspaces += 1
            if nspaces == 1:
                result += '%20'
        else:
            nspaces = 0
            if char.lower() in ascii_hex:
                if not result.endswith(ascii_hex[char]):
                    result += ascii_hex[char]
            else:
                result += char

    return result
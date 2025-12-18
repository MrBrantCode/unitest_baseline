"""
QUESTION:
Create a function `convert_to_camel_case(s)` that takes a string `s` as input and returns the string converted to CamelCase. The input string may contain multiple words separated by spaces, dashes, or underscores, and may include special characters, numbers, leading and trailing spaces, dashes, or underscores, and multiple consecutive spaces, dashes, or underscores. The function should not use built-in string conversion functions or libraries, should handle strings of any length and with mixed casing, and should have a efficient runtime complexity.
"""

def convert_to_camel_case(s):
    s = s.strip(' -_')
    result = ""
    capitalize_next = False

    for i, c in enumerate(s):
        if c in ' -_':
            capitalize_next = True
        elif c.isalpha() or c.isdigit():
            if capitalize_next:
                result += c.upper()
                capitalize_next = False
            else:
                result += c

    return result
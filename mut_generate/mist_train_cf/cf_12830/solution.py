"""
QUESTION:
Write a function named `format_string` that takes a string `x` as input. For each character in the string, if it's alphabetic, convert it to uppercase, if it's a digit, multiply it by 2 and convert it to a string, and if it's neither, leave it as is. Return a string in the format "The output is: {}" with the modified characters.
"""

def format_string(x):
    result = ""
    for char in x:
        if char.isalpha():
            result += char.upper()
        elif char.isdigit():
            result += str(int(char) * 2)
        else:
            result += char
    return "The output is: {}".format(result)
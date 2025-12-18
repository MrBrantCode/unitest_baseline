"""
QUESTION:
Write a function `print_lower_asterisks` that takes a string as input and returns the string with all asterisks in lowercase. The function must use recursion and cannot use any built-in string manipulation functions, regular expressions, or loops.
"""

def print_lower_asterisks(string):
    if string == '':
        return ''
    elif string[0] == '*':
        return '*' + print_lower_asterisks(string[1:])
    else:
        return string[0] + print_lower_asterisks(string[1:])
"""
QUESTION:
Create a function named `count_capital_letters` that takes a list of strings as input and returns the count of capital letters in the list, ignoring any capital letters within parentheses and considering capital letters with accents or special characters. The function should handle strings containing non-alphabetic characters and nested parentheses.
"""

def count_capital_letters(strings):
    count = 0
    open_parentheses = 0

    for string in strings:
        for char in string:
            if char == '(':
                open_parentheses += 1
            elif char == ')':
                open_parentheses -= 1
            elif open_parentheses == 0 and char.isupper():
                count += 1

    return count
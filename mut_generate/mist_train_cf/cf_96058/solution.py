"""
QUESTION:
Create a function `count_capital_letters(strings)` to count the number of capital letters in a given list of strings. The function should ignore any capital letters within parentheses (including nested ones) and consider capital letters with accents or special characters.
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
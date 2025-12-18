"""
QUESTION:
Create a function `count_capital_letters(strings)` that takes a list of strings as input and returns the total count of capital letters in the list. The function should ignore non-alphabetic characters and capital letters within parentheses.
"""

def count_capital_letters(strings):
    count = 0
    for string in strings:
        for char in string:
            if char.isalpha() and char.isupper() and not (string.startswith("(") and string.endswith(")")):
                count += 1
    return count
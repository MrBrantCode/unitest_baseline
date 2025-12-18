"""
QUESTION:
Write a function `find_xy_lexemes` that finds all lexemes within a given textual data set that exhibit the characteristic of possessing the Latin-derived alphabetic characters 'x' and 'y' in immediate sequence within a certain range of characters, ignoring case sensitivity, special characters, numbers, and blanks.
"""

import re

def find_xy_lexemes(text):
    pattern = '[^a-zA-Z]*x[^a-zA-Z]*y[^a-zA-Z]*'
    matches = re.findall(pattern, text, re.I)

    lexemes = []
    for match in matches:
        lexeme = re.sub('[^a-zA-Z]', '', match)
        lexemes.append(lexeme)

    return lexemes
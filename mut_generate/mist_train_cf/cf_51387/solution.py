"""
QUESTION:
Create a function named `find_positions` that takes two parameters: a string `text` and a substring. The function should return a list of all positions where the substring occurs in the text, considering overlapping occurrences. The positions are 0-indexed.
"""

def find_positions(text, substring):
    positions = []
    i = text.find(substring)

    while i != -1:
        positions.append(i)
        i = text.find(substring, i+1)

    return positions
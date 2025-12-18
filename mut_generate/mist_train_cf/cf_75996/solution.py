"""
QUESTION:
Write a function called `find_symbol_occurrences` that identifies every occurrence of a specified character within a given passage and returns a list of indices where the character is found. The function should take two parameters: `text` and `symbol`.
"""

def find_symbol_occurrences(text, symbol):
    occurrences = []
    for i in range(len(text)):
        if text[i] == symbol:
            occurrences.append(i)
    return occurrences
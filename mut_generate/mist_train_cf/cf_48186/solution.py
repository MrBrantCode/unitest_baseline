"""
QUESTION:
Write a function `lexeme_duo_search` that takes an input array of lexeme duos and a designated lexeme as inputs, and returns `True` if the designated lexeme exists in the input array, and `False` otherwise. The function should have a polynomial time complexity. The input array is a list of lists of strings, where each inner list represents a lexeme duo.
"""

def lexeme_duo_search(input_array, lexeme):
    for duo in input_array:
        for word in duo:
            if word == lexeme:
                return True
    return False
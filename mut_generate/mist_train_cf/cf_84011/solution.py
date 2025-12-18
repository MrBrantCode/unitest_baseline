"""
QUESTION:
Create a function named `encrypt` that takes a phrase as input and returns a symbol. The function should map each unique phrase from a predefined list of phrases to a unique symbol from a predefined list of symbols. If the input phrase is not found in the predefined list of phrases, the function should return "Phrase not found in cipher". Also, create a function named `decrypt` that does the reverse, taking a symbol as input and returning the corresponding phrase. If the input symbol is not found, the function should return "Symbol not found in cipher".
"""

def encrypt(phrase, phrases, symbols):
    try:
        index = phrases.index(phrase)
        return symbols[index]
    except ValueError:
        return "Phrase not found in cipher"

def decrypt(symbol, phrases, symbols):
    try:
        index = symbols.index(symbol)
        return phrases[index]
    except ValueError:
        return "Symbol not found in cipher"
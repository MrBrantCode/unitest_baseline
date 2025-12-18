"""
QUESTION:
Create a function `transmute_punctuation` that takes a string `text` as input and replaces the punctuation symbols `.`, `,`, `?`, and `!` with their corresponding verbal phrases `dot`, `comma`, `question mark`, and `exclamation mark`, respectively. The function should return the modified string.
"""

def transmute_punctuation(text):
    punctuation_dict = {".": " dot ", ",": " comma ", "?": " question mark ", "!": " exclamation mark "}
    for symbol, phrase in punctuation_dict.items():
        text = text.replace(symbol, phrase)
    return text
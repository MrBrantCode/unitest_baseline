"""
QUESTION:
Write a function `punctuation_to_words` that takes a string input and returns the input string with specific punctuations (., !, ?, ', ", :, ;) replaced by their respective English word representations. The function should handle sentences with multiple punctuations, preserve the original case, and replace multiple spaces with a single space. The implementation should not use any external libraries in Python.
"""

def punctuation_to_words(sentence):
    punctuation_dict = {'.': ' dot ',
                        ',': ' comma ',
                        '!': ' exclamation mark ',
                        '?': ' question mark ',
                        "'": ' single quote ',
                        '"': ' double quote ',
                        ':': ' colon ',
                        ';': ' semicolon '}

    for punctuation, word in punctuation_dict.items():
        sentence = sentence.replace(punctuation, word)

    sentence = ' '.join(sentence.split())
    return sentence